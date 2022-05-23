import socket
client = socket.socket()
client.connect(('127.0.0.1',8989))
for i in range(10):
    client.send(b'moran')
    print(client.recv(1024))