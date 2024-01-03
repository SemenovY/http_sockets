import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 8080))
sock.listen(5)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
# sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)


client, addr = sock.accept()
result = client.recv(1024)
client.close()
print(result.decode('utf-8'))
