import sys
import os
import socket
from helpers.MIME import MIME_dict

if len(sys.argv) == 2:
    port = sys.argv[1]
else:
    port = 28333

fnf_response = "HTTP/1.1 404 Not Found\r\nContent-Type: text/plain\r\nContent-Length: 13\r\nConnection: close\r\n\r\n404 not found\r\n"
fnf_response = fnf_response.encode("ISO-8859-1")
delim = b"\r\n\r\n"
Content = MIME_dict

with socket.socket() as s:
    s.bind(('', port))
    s.listen()

    while True:
        msg = b""
        new_conn = s.accept()
        new_socket = new_conn[0]

        while delim not in msg:
            msg += new_socket.recv(4096)

        msg = msg.decode("ISO-8859-1")
        lines = msg.split("\r\n")
        get = lines[0].split()
        file_ext = os.path.split(get[1])
        file = file_ext[1]

        ext = os.path.splitext(file)
        mime_type = Content[ext[1]]

        try:
            with open("files\\"+file) as fp:
                data = fp.read()
        except Exception:
            new_socket.sendall(fnf_response)
            new_socket.close()
            continue

        data = data.encode("ISO-8859-1")
        length = str(len(data))
        data = data.decode("ISO-8859-1")

        response = "HTTP/1.1 200 OK\r\nContent-Type: "+mime_type+"\rContent-Length: "+length+"\r\nConnection: close\r\n\r\n"+data+"\r\n"
        response = response.encode("ISO-8859-1")

        new_socket.sendall(response)
        new_socket.close()
