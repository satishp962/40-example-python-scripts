import socket

s = socket.socket()
host = socket.gethostname()
port = 12345

s.connect((host, port))
s.send(bytes("RabinKarp".encode()))
msg = s.recv(1024)
print("Message recieved: ", msg.decode('utf8'))
s.close()