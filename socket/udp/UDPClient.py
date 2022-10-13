from socket import *

serverName = 'localhost'
serverPort1 = 12001
serverPort2 = 12002


def demo():
    # AF_INET: IPv4
    # SOCK_DGRAM: UDP
    # UDP 的套接字是二元的
    client_socket = socket(AF_INET, SOCK_DGRAM)

    sentence = input('Input sentence: ')
    print('original message: ', sentence)

    client_socket.sendto(sentence.encode(), (serverName, serverPort1))
    modified_message_1, server_address_1 = client_socket.recvfrom(2048)
    print('received from server1: ', modified_message_1.decode())

    client_socket.sendto(sentence.encode(), (serverName, serverPort2))
    modified_message_2, server_address_2 = client_socket.recvfrom(2048)
    print('received from server2: ', modified_message_2.decode())

    client_socket.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    demo()
