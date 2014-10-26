import sys
import socket


def send_message(msg):
    try:
        client_socket = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM,
            socket.IPPROTO_IP)
        try:
            client_socket.connect(('127.0.0.1', 50000))
            client_socket.sendall(msg)
        finally:
            client_socket.shutdown(socket.SHUT_WR)
    finally:
        client_socket.close()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "usage: %s <msg>", (sys.argv[0])
    send_message(sys.argv[1])
