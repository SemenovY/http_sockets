import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 8080))
sock.listen(5)

sock.setblocking(False) # If not client, raise exeption error!


client, addr = sock.accept()
result = client.recv(1024)
client.close()
print(result.decode('utf-8'))
