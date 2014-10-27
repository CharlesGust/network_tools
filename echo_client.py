import sys
import socket


def send_message(msg):
    buffsize = 128
    address = ('127.0.0.1', 50000)

    try:
        client_socket = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM,
            socket.IPPROTO_IP)

        client_socket.connect(address)
        client_socket.sendall(msg)
        client_socket.shutdown(socket.SHUT_WR)

        while True:
            data = client_socket.recv(buffsize)
            if data:
                print data,
            else:
                break

    finally:
        client_socket.close()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "usage: %s <msg>", (sys.argv[0])
    else:
        send_message(sys.argv[1])
