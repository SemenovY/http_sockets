import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(b'HEEEELLO', ('127.0.0.1', 8888))
