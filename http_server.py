import socket


def http_ok():
    return "HTTP/1.1 200 OK \r\n"


def http_error(status_code, reason_phrase):
    return "HTTP/1.1 %03d %s \r\n" % (status_code, reason_phrase)


def check_request(req):
    check_meth = req.partition(' ')
    if check_meth[0] != "GET":
        return False, http_error(405, "Method Not Allowed")
    check_prot = check_meth[2].partition(' ')
    if check_prot[2] != "HTTP/1.1":
        return False, http_error(501, "Not Implemented")
    return True, check_prot[0]


def listen():
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
                        succeeded, msg = check_request(data)
                        if not succeeded:
                            conn.sendall(msg)
                            break
                        else:
                            conn.sendall(http_ok())

                        # here is where server would process uri
                        print msg

                    else:
                        break
            finally:
                conn.shutdown(socket.SHUT_RDWR)
                conn.close()
    finally:
        server_socket.close()

if __name__ == "__main__":
    listen()
