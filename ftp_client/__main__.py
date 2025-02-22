# FTP_CLIENT
# Philip Picard, Zac Laymon, Justin Keller, Tyler Hay
# Data Comm, Bhuse
# 2/8/2020

import socket
import io

def client():


    flag = True
    connected = False

    # making the socket
    client_socket = socket.socket()

    #loop to continuously accept user input.
    while(flag):
        print("Enter a command (CONNECT, LIST, RETRIEVE, STORE, QUIT): ")
        userInput = str(input())

        command = userInput.split()

        if len(command) == 0:
            pass
        elif(command[0] == "connect" or command[0] == "CONNECT"):

            if(len(command) != 3):
                print("CONNECT format: connect <HOST NAME> <PORT NO>")
            else:
                # getting host by name
                host = command[1]
                # converting port number to an integer
                port = int(command[2])

                try:
                    client_socket.connect((host, port))
                    connected = True
                    print("Connected to: " + str(host) + ":" + str(port) + "\n")
                except:
                    print("Failed to connect to server.")

        elif(command[0] == "list" or command[0] == "LIST"):
            if not connected:
                print("Please connect to server.\n")
            else:
                client_socket.sendall(userInput.encode())
                # Wait for the response from the server.
                print(client_socket.recv(1024).decode())
                # print("\n")

        elif (command[0] == "retrieve" or command[0] == "RETRIEVE"):
            if(len(command) != 2):
                print("RETRIEVE format: retrieve <filename>")
            elif not connected:
                print("Please connect to server.")
            else:
                client_socket.sendall(userInput.encode())

                # Wait for the response from the server.
                print(client_socket.recv(1024).decode())

                # Receiving data from server and writing to file.
                data = client_socket.recv(4096)
                with open(command[1], 'wb+') as f:
                    f.write(data)
                    print("File Retrieved: saved as " + command[1] + "\n")



        elif (command[0] == "store" or command[0] == "STORE"):
            if (len(command) != 2):
                print("RETRIEVE format: retrieve <filename>")
            elif not connected:
                print("Please connect to server.")
            else:
                # send command to server
                client_socket.sendall(userInput.encode())

                # Wait for the response from the server.
                print(client_socket.recv(1024).decode())

                file = command[1]
                f = open(file, "rb")

                client_socket.sendall(f.read())


        elif (command[0] == "quit" or command[0] == "QUIT"):
            try:
                client_socket.sendall(userInput.encode())
            except:
                # If client was not connected, a broken pipe exception will be raised.
                pass
            #just need to break the loop
            break
        
        else:
            print("Command not recognised.\nValid commands: CONNECT, LIST, RETRIEVE, STORE, QUIT, EXIT")

    client_socket.close()


client()
