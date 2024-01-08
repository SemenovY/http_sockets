# Client
import socket


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('example.com', 80))
content_items = [
    'GET / HTTP/1.1',
    'Host: example.com',
    'Connection: keep-alive',
    'Accept: text/html',
    '\n'
]
content = '\n'.join(content_items)
print('---HTTP Message---')
print(content)
print('---End of HTTP Message---')
sock.send(content.encode('utf-8'))
result = sock.recv(10024)
print(result.decode())
