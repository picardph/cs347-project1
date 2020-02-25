import socket
import threading
import os


class FileServerHandler(object):

    # Define the properties of each socket to support multithreading
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind((self.host, self.port))


    # server handles all client commands using sub-methods
    def handle(self, client, address):


       def sendFile(user, fileName):
            print("Client requested file: " + str(fileName))
            # tell the client to continue
            user.send("continue".encode())
            try:
                f = open(fileName, "rb")
                user.sendall(f.read())

            except:
                print("File not found")


       def storeFile(user, file):

            print("Storing File: " + str(file) + "\n")

            # tell the client to continue
            user.send("continue".encode())

            try:
                data = user.recv(4096)
                with open(file, 'wb+') as f:
                    f.write(data)
                    print("File successfully stored!\n")
            except:
                print("File not found")

       def list(user):

            response = ""
            for f in os.listdir(os.curdir):
                response += f + "\n"
            user.sendall(response.encode())

        # Loop for server to continuously take commands
       while True:

            try:
                data = client.recv(1024).decode()
                data = data.split(' ')
                print("Received command from client.")

                if not data:
                    break

                if data[0] == 'list' or data[0] == 'LIST':
                    list(client)

                if data[0] == 'quit' or data[0] == 'QUIT':
                    client.close()
                    break

                if data[0] == 'retrieve' or data[0] == 'RETRIEVE':
                    sendFile(client, data[1])

                if data[0] == 'store' or data[0] == 'STORE':
                    storeFile(client, data[1])


            except:
                print("Connection closed from: " + str(address))
                client.close()
                break

    # allows the server to listen for multiple sockets and crate multiple threads
    def listenForSockets(self):
        self.socket.listen(3)

        while True:
            client, address = self.socket.accept()
            print("Connection accepted From: " + str(address))

            client.settimeout(30)
            threading.Thread(target = self.handle, args = (client, address)).start()




host = "localhost"
port = 2468
print("======================================")
print("Server is running on port number: %d" % port)
print ("Awaiting client connection...")
print("======================================")
FileServerHandler(host, port).listenForSockets()
