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


host, port = "localhost", 2468
tcp_server = socketserver.TCPServer((host, port), FileServerHandler)

try:
    tcp_server.serve_forever()
except KeyboardInterrupt:
    tcp_server.shutdown()
    tcp_server.server_close()
