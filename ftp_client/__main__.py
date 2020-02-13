# FTP_CLIENT
# Philip Picard, Zac Laymon, Justin Keller, Tyler Hay
# Data Comm, Bhuse
# 2/8/2020

import socket

def client():
    flag = 1

    #Get the Host name
    host = socket.gethostname()

    #socket server port number
    port = 2468

    # making the socket and connecting to the server
    client_socket = socket.socket()
    client_socket.connect((host, port))

    #loop to continuously accept user input.
    while(flag):

        print("Enter A Command: ")
        userInput = str(input())

        command = userInput.split()

        if(command[0] == "connect" or command[0] == "CONNECT"):

            if(len(command) != 3):
                print("CONNECT format: connect <HOST NAME> <PORT NO>")
            else:
                client_socket.send(userInput.encode())
        if(command[0] == "list" or command[0] == "LIST"):
            client_socket.send(userInput.encode())

        if (command[0] == "retrieve" or command[0] == "RETRIEVE"):
            if(len(command) != 2):
                print("RETRIEVE format: retrieve <filename>")
            else:
                client_socket.send(userInput.encode())


        if (command[0] == "store" or command[0] == "STORE"):
            if (len(command) != 2):
                print("RETRIEVE format: retrieve <filename>")
            else:
                client_socket.send(userInput.encode())

        if (command[0] == "quit" or command[0] == "QUIT"):
            client_socket.send(userInput.encode())

        #loop break to end program
        if(command[0] == "exit"):
            flag = 0

        #display response from server
        server_data = client_socket.recv(1024).decode()

        # print the data to terminal
        print('Received from server: ' + server_data)

    #out of loop: close socket before termination
    client_socket.close()
