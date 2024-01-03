# example1 udp server socket
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', 8888))
result = sock.recv(1024)
print('Message received:', result.decode('utf-8'))
sock.close()
