import socket


def echo():
    try:
        server_socket = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM,
            socket.IPPROTO_IP)
        server_socket.bind(('127.0.0.1', 50000))
        while True:
            server_socket.listen(1)
            try:
                conn, addr = server_socket.accept()
                print conn.recv(256)
            finally:
                conn.close()
    finally:
        server_socket.close()

if __name__ == "__main__":
    echo()
