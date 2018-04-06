import socket

s = socket.socket()
host = socket.gethostname()
port = 12345
s.bind((host, port))

s.listen(5)

while True:
    c, addr = s.accept()
    print("Connected to client")

    while True:
        msg = input("Enter message: ")
        c.send(bytes(msg.encode()))
        msg = c.recv(1024)
        print('Message recieved: ', msg.decode("utf-8"))