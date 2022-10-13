from socket import *


def demo():
    server_port = 12001
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.bind(('', server_port))
    server_socket.listen(1)
    print("TCP server ready, port: ", server_port)

    while True:
        connection_socket, address = server_socket.accept()
        sentence = connection_socket.recv(2048)
        print("message from client: --------------, client address: ", address)
        print(sentence.decode())
        print("message end ------------------------------")
        modified_sentence = sentence.decode().upper()
        connection_socket.send(modified_sentence.encode())
        connection_socket.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    demo()
