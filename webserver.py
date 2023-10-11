import sys
import socket

if len(sys.argv) == 2:
    port = sys.argv[1]
else:
    port = 28333

response = "HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: 6\r\nConnection: close\r\n\r\nHello!\r\n"
response = response.encode("ISO-8859-1")
delim = b"\r\n\r\n"

with socket.socket() as s:
    s.bind(('', port))
    s.listen()

    while True:
        msg = b""
        new_conn = s.accept()
        new_socket = new_conn[0]

        while delim not in msg:
            msg += new_socket.recv(4096)

        new_socket.sendall(response)
        new_socket.close()
