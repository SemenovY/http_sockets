# example1 udp client socket
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(b'Hello World!', ('127.0.0.1', 8888))
