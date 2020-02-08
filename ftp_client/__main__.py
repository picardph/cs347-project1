# FTP_CLIENT
# Philip Picard, Zac Laymon, Justin Keller, Tyler Hay
# Data Comm, Bhuse
# 2/8/2020

flag = 1

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