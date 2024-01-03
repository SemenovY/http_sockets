import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 8080))
sock.listen(5)
sock.setblocking(False)

while True:
    try:
        client, addr = sock.accept()
    except socket.error:
        print('no client connected')
    except KeyboardInterrupt:
        break
    else:
        # sock.setblocking(True)
        result = client.recv(1024)
        client.close()
        print(result.decode('utf-8'))
