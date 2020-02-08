import socket

soc = None
ip = '127.0.0.1'
port = 3927

def Connect(ip=ip, port=port):
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.connect(ip, port)
    print("Connected to " + str(ip) + ":" + port)


def List():
    pass

def Retrieve(fileName):
    pass

def Store():
    pass

def End():
    pass