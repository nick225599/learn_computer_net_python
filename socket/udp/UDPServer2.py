from socket import *


def demo():
    server_port = 12002
    server_socket = socket(AF_INET, SOCK_DGRAM)
    server_socket.bind(('', server_port))
    print("UDP server2 ready, port: ", server_port)

    while True:
        message, client_address = server_socket.recvfrom(2048)
        print("message from client: ", message.decode())
        modified_message = message.decode().lower()
        server_socket.sendto(modified_message.encode(), client_address)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    demo()
