# FTP_CLIENT
# Philip Picard, Zac Laymon, Justin Keller, Tyler Hay
# Data Comm, Bhuse
# 2/8/2020

import socket

soc = None
ip = '127.0.0.1'
port = 3927
flag = 1

def Connect(ip=ip, port=port):
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.connect((ip, port))
    print("Connected to " + str(ip) + ":" + str(port))

def List():
    pass

def Retrieve(fileName):
    pass

def Store():
    pass

def End():
    pass

#loop to continuously accept user input.
while(flag):

    print("Enter A Command")
    userInput = str(input())

    command = userInput.split()

    if(command[0] == "connect" or command[0] == "CONNECT"):

        if(len(command) != 3):
            print("CONNECT format: connect <IP ADDRESS> <PORT NO>")
        else:
            print("hey")
    if(command[0] == "list" or command[0] == "LIST"):
        print("hey")

    if (command[0] == "retrieve" or command[0] == "RETRIEVE"):
        if(len(command) != 2):
            print("RETRIEVE format: retrieve <filename>")
        else:
            print("hey")


    if (command[0] == "store" or command[0] == "STORE"):
        if (len(command) != 2):
            print("RETRIEVE format: retrieve <filename>")
        else:
            print("hey")

    if (command[0] == "quit" or command[0] == "QUIT"):
        print("hey")

    #loop break to end program
    if(command[0] == "exit"):
        flag = 0