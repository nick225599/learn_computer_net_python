# import socket module
from socket import *

serverSocket = socket(AF_INET, SOCK_STREAM)

# Prepare a sever socket
serverSocket.bind(('', 80))
serverSocket.listen(1)

while True:

    # Establish the connection
    print('Ready to serve...')

    connectionSocket, addr = serverSocket.accept()
    message = connectionSocket.recv(2048).decode()
    print("message: ")
    print(message)
    filename = message.split()[1]
    print("fileName: ", filename)
    f = open(filename[1:])
    outputdata = f.readline()  # Fill in start #Fill in end
    # Send one HTTP header line into socket
    # Fill in start
    # Fill in end
    # Send the content of the requested file to the client
    for i in range(0, len(outputdata)):
        connectionSocket.send(outputdata[i].encode())
    connectionSocket.send("\r\n".encode())
    connectionSocket.close()
