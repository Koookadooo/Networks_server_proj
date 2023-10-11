import sys
import socket

if len(sys.argv) == 3:
    host = sys.argv[1]
    port = int(sys.argv[2])
else:
    host = sys.argv[1]
    port = 80

get = "GET / HTTP/1.1\r\nHost: " + host + "\r\nConnection: close\r\n\r\n"
get_r = get.encode("ISO-8859-1")

with socket.socket() as s:
    s.connect((host, port))
    s.sendall(get_r)

    while True:
        message = s.recv(4096)
        print(message.decode("ISO-8859-1"))
        if not message:
            break

    s.close()
