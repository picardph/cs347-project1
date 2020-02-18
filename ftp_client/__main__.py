# FTP_CLIENT
# Philip Picard, Zac Laymon, Justin Keller, Tyler Hay
# Data Comm, Bhuse
# 2/8/2020

import socket

def client():


    flag = True
    connected = False

    #Get the Host name
    host = None

    #socket server port number
    port = None

    # making the socket
    client_socket = socket.socket()

    #loop to continuously accept user input.
    while(flag):

        print("Enter A Command: ")
        userInput = str(input())

        command = userInput.split()

        if(command[0] == "connect" or command[0] == "CONNECT"):

            if(len(command) != 3):
                print("CONNECT format: connect <HOST NAME> <PORT NO>")
            else:
                host = command[1]
                #converting port number to an integer
                port = int(command[2])
                client_socket.connect((host, port))
                connected = True

        if(command[0] == "list" or command[0] == "LIST"):
            if(connected == False):
                print("Please Connect to Server")
            else:
                client_socket.sendall(userInput.encode("utf-8"))
                # Wait for the response from the server.
                print(client_socket.recv(1024).decode("utf-8"))

        if (command[0] == "retrieve" or command[0] == "RETRIEVE"):
            if(len(command) != 2):
                print("RETRIEVE format: retrieve <filename>")
            elif(connected == False):
                print("Please Connect to Server")
            else:
                client_socket.send(userInput.encode())


        if (command[0] == "store" or command[0] == "STORE"):
            if (len(command) != 2):
                print("RETRIEVE format: retrieve <filename>")
            elif (connected == False):
                print("Please Connect to Server")
            else:
                client_socket.sendfile(userInput)

        if (command[0] == "kill_server" and connected):
            client_socket.sendall("kill_server".encode("utf-8"))

        if (command[0] == "quit" or command[0] == "QUIT"):
            client_socket.send(userInput.encode())
            client_socket.detach()

        #loop break to end program
        if(command[0] == "exit"):
            flag = 0

        #display response from server
        #if connected:
            #server_data = client_socket.recv(1024).decode()

        # print the data to terminal
        #print('Received from server: ' + server_data)

    #out of loop: close socket before termination
    client_socket.close()


client()