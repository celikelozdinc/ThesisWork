import Operations, time, threading, socket, pika, json, subprocess, sys

class Client:
    # __init__ is known as the constructor
    def __init__(self, currentFlow, jobId):
        print("Constuctor of Client class has been called")
        self.currentFlow = currentFlow
        self.jobId = jobId
        self.containerIPQuery = "ip a show eth0 | grep -w inet | awk '{print $2'}"
        #self.containerIP = subprocess.Popen(self.containerIPQuery, shell=True, stdout=subprocess.PIPE, stderr = subprocess.PIPE).communicate()
        self.containerIP = subprocess.check_output(self.containerIPQuery,shell=True).decode(sys.stdout.encoding).strip().split('/')[0]
        self.startState = Operations.StartState.StartState()
        self.copyState = Operations.CopyState.CopyState()
        self.finishState = Operations.FinishState.FinishState()
        self.startState.setJobId(jobId)
        """
        self.socketObj = socket.socket()  # Create a socket object
        self.host = socket.gethostname()  # Get local machine name
        self.port = 2347  # Reserve a port for your service.
        """

    @staticmethod
    def CopyThread(copyState):
        print("Starting Copy Thread")
        copyState.DoJob()
        time.sleep(1.1)
        print("Exiting Copy Thread")

    @staticmethod
    def DumpThread(copyState):
        print("Starting Dump Thread")
        x, y = copyState.DoDump()  
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))      
        channel = connection.channel()
        channel.queue_declare(queue='sync')
        increment = {"x": str(x), "y":str(y)}
        message = json.dumps(increment)
        channel.basic_publish(exchange='', routing_key='sync', body=message)
        print(" [x] Sent 'Increment From client process!' ")
        connection.close()
        time.sleep(2.2)
        print("Exiting Dump Thread")

    def startStateMachine(self):

        """
        self.socketObj.connect((self.host, self.port))
        message = input(" -> ")  # take input
        self.socketObj.send(message.encode())  # send message
        # data =  self.socketObj.recv(1024).decode()  # receive response
        # print('Received from server: ' + data)  # show in terminal
        # message = input(" -> ")  # again take input
        self.socketObj.close() # Close the socket when done
        """

        connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
        channel = connection.channel()
        channel.queue_declare(queue='myQueue')
        data = \
            {
                "id": 1,
                "name": "Client Description",
                "description": "Hello from client process " + str(self.containerIP)
            }
        message = json.dumps(data)
        channel.basic_publish(exchange='', routing_key='myQueue', body=message)
        print(" [x] Sent 'Json From client process!'")
        connection.close()

        self.startState.echo()
        self.finishState.echo()
        print(self.finishState.getJobId())
        # Create two threads #
        delay = 60 * 15  # for 15 minutes processing
        close_time = time.time() + delay
        self.startState.DoJob()

        while True:
            if time.time() > close_time:
                break
            threading.Thread(name='CopyThread', target=self.CopyThread(self.copyState)).start()
            threading.Thread(name='DumpThread', target=self.DumpThread(self.copyState)).start()

        self.finishState.DoJob()
        #                    #
