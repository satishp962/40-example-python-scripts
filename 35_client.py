import socket

s = socket.socket()
host = socket.gethostname()
port = 12345

s.connect((host, port))

while True:
    msg = s.recv(1024)
    print("Server: ", msg.decode('utf8'))  
    msg = input("Enter message: ")
    s.send(bytes(msg.encode()))