import Operations, time, threading, socket

class Client:
    # __init__ is known as the constructor
    def __init__(self, currentFlow, jobId):
        print("Constuctor of Client class has been called")
        self.currentFlow = currentFlow
        self.jobId = jobId
        self.startState = Operations.StartState.StartState()
        self.copyState = Operations.CopyState.CopyState()
        self.finishState = Operations.FinishState.FinishState()
        self.startState.setJobId(jobId)
        self.socketObj = socket.socket()  # Create a socket object
        self.host = socket.gethostname()  # Get local machine name
        self.port = 2347  # Reserve a port for your service.

    @staticmethod
    def CopyThread(copyState):
        print("Starting Copy Thread")
        copyState.DoJob()
        time.sleep(1.1)
        print("Exiting Copy Thread")

    @staticmethod
    def DumpThread(copyState):
        print("Starting Dump Thread")
        copyState.DoDump()
        time.sleep(2.2)
        print("Exiting Dump Thread")

    def startStateMachine(self):

        self.socketObj.connect((self.host, self.port))
        message = input(" -> ")  # take input
        self.socketObj.send(message.encode())  # send message
        # data =  self.socketObj.recv(1024).decode()  # receive response
        # print('Received from server: ' + data)  # show in terminal
        # message = input(" -> ")  # again take input
        self.socketObj.close() # Close the socket when done


        self.startState.echo()
        self.finishState.echo()
        print(self.finishState.getJobId())
        # Create two threads #
        delay = 60 * 0.5  # for 0.5 minute delay
        close_time = time.time() + delay
        self.startState.DoJob()

        while True:
            if time.time() > close_time:
                break
            threading.Thread(name='CopyThread', target=self.CopyThread(self.copyState)).start()
            threading.Thread(name='DumpThread', target=self.DumpThread(self.copyState)).start()

        self.finishState.DoJob()
        #                    #