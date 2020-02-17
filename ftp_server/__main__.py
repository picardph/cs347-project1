import socket
import socketserver
import os


class FileServerHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data: str = self.request.recv(1024).strip()
        data.split(' ')
        response = ''
        if data[0] == 'list' or data[0] == 'LIST':
            for f in os.listdir(''):
                response += f + ' '
            response.strip()
        self.request.sendall(response.encode())


host, port = "localhost", 2468
tcp_server = socketserver.TCPServer((host, port), FileServerHandler)
tcp_server.serve_forever()