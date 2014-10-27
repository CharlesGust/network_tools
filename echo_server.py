import socket


def http_ok():
    return "HTTP/1.1 200 OK \r\n"


def http_error(status_code, reason_phrase):
    return "HTTP/1.1 %03d %s \r\n" % (status_code, reason_phrase)


def echo():
    buffsize = 128
    address = ('127.0.0.1', 50000)

    try:
        server_socket = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM,
            socket.IPPROTO_IP)
        server_socket.bind(address)
        server_socket.listen(1)

        while True:
            conn, addr = server_socket.accept()
            try:
                while True:
                    data = conn.recv(buffsize)
                    if data:
                        conn.sendall(data)
                    else:
                        break
            finally:
                conn.shutdown(socket.SHUT_RDWR)
                conn.close()
    finally:
        server_socket.close()

if __name__ == "__main__":
    echo()
