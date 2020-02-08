import socket

ip = '127.0.0.1'
port = 3927

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((ip, port))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(str(addr) + " connected.")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
