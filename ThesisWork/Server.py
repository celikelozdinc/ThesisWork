import socket, pika, json


class Server:
    # __init__ is known as the constructor
    def __init__(self):
        print("Constuctor of Server class has been called")
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue='myQueue')
        self.channel.queue_declare(queue='sync')
        # Store the changes on each container(client) #
        self.checkPointDict = dict()
        """
        self.socketObj = socket.socket()  # Create a socket object
        self.host = socket.gethostname()  # Get local machine name
        self.port = 2347  # Reserve a port for your service.
        self.socketObj.bind((self.host, self.port))  # Bind to the port
        """

    def callback(self,ch, method, properties, body):
        data = json.loads(body)
        print("ID: {}".format(data['id']))
        print("Name: {}".format(data['name']))
        print('Description: {}'.format(data['description']))
        print("Container IP: {}".format((data['containerIP'])))
        containerIP = str(data['containerIP'])
        if containerIP in self.checkPointDict:
            print("CKPTs for this container are already stored.")
        else:
            print("CKPTs for this container will be stored from now on.")
            self.checkPointDict[containerIP] = []

    def sync_callback(self,ch,method,properties,body):
        sync_data = json.loads(body)
        print("X To Be Dumped: {}".format(sync_data['x']))
        print("Y To Be Dumped: {}".format(sync_data['y']))
        print("ContainerIP To Be Dumped: {}".format(sync_data['containerIP']))
        containerIP = str(sync_data['containerIP'])
        if containerIP in self.checkPointDict:
            print("CKPTs for this container are already stored. We'll append a new CKPT.")
            t = tuple((str(sync_data['x']),str(sync_data['y'])))
            self.checkPointDict[containerIP].append(t)
        else:
            print("FATAL ERROR. You are trying to CKPT to another client.")

    def startServer(self):
        print("Server is started. ")
        self.channel.basic_consume(queue='myQueue', on_message_callback=self.callback, auto_ack=True)
        self.channel.basic_consume(queue='sync', on_message_callback=self.sync_callback, auto_ack=True)
        print("Server is started consuming. ")
        self.channel.start_consuming()

        """
        self.socketObj.listen(3)  # Now wait for client connection.
        while True:
            clientSocket, address = self.socketObj.accept()  # Establish connection with client.
            print("Got connection from: ", address)
            data = clientSocket.recv(1024).decode()
            if not data:
                print("Data is not received from client. Break.")
                break
            print("from connected user: " + str(data))
            # data = input(' -> ')
            # clientSocket.send(data.encode())  # send data to the client
        clientSocket.close()  # Close the connection
        """

