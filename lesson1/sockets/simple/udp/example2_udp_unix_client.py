# example2 udp unix client
import socket

sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
sock.sendto(b'Hello World!', 'unix.sock')
