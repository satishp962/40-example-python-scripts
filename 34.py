import socket

s = socket.socket()
host = socket.gethostname()
port = 12345
s.bind((host, port))

s.listen(5)

c, addr = s.accept()
print("Connected to client")
msg = c.recv(1024)
print('Message recieved: ', msg.decode("utf-8"))
msg = msg.upper()
c.send(bytes(msg))
c.close()