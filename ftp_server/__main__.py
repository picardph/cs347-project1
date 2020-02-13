import socket

def server():

    host = socket.gethostname()
    port = 2468

    #create the socket
    server_socket = socket.socket()

    #bind the socket using the host and port number
    server_socket.bind((host, port))

    #listen for 2 clients
    server_socket.listen(2)

    #accepting connections
    connection, address = server_socket.accept()
    print("Connection from: " + str(address))

    #keep looping
    while True:
        # receive data stream with packets up to 1024 bytes
        data = connection.recv(1024).decode()
        if not data:
            # if data is not received then break out of loop
            break
        print("From connected user: " + str(data))
        data = input(' -> ')
        # send data to the client
        connection.send(data.encode())

    # Out of loop: close connection
    connection.close()