# example3 tcp socket client
import socket


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('', 8080))
sock.send(b'Hello World!')
sock.close()
