import socketserver
import os


class FileServerHandler(socketserver.BaseRequestHandler):
    def handle(self):
        print("Got data from client.")
        data = self.request.recv(1024).decode("utf-8")
        data = data.split(' ')
        response = ''
        if data[0] == 'list' or data[0] == 'LIST':
            for f in os.listdir(os.curdir):
                response += f + ' '
            response.strip()
            self.request.sendall(response.encode())
        if data[0] == 'retrieve' or data[0] == 'RETRIEVE':
            self.sendFile(data[1])


    def sendFile(self, fileName):
        print("Client requested file: " + str(fileName))
        try:
            f = open(fileName, 'rb')
            data = f.read(1024)
            while data != b'':
                self.request.sendall(data)
                data = f.read(1024)
            #self.request.sendall(b'')
            
            # Waiting for client to notify data transfer has finished.
            #self.request.recv(1024)
            #self.request.sendall(b"File sent.")
            f.close()
        except:
            print("File not found")
            #self.request.sendall(b'')
            #self.request.recv(1024)
            #self.request.sendall("File not found.".encode())


host, port = "localhost", 2468
tcp_server = socketserver.TCPServer((host, port), FileServerHandler)

try:
    tcp_server.serve_forever()
except KeyboardInterrupt:
    tcp_server.shutdown()
    tcp_server.server_close()
