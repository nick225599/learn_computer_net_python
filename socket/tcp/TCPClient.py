from socket import *

serverName = 'localhost'
serverPort = 12001



def demo():
    # AF_INET: IPv4
    # SOCK_DGRAM: UDP
    # TCP 的套接字是四元的
    client_socket = socket(AF_INET, SOCK_STREAM)
    client_socket.connect((serverName, serverPort))

    sentence = input('Input sentence: ')
    print('original sentence: ', sentence)

    client_socket.sendto(sentence.encode(), (serverName, serverPort))
    modified_message, server_address = client_socket.recvfrom(2048)
    print('received from server: ', modified_message.decode())

    client_socket.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    demo()
