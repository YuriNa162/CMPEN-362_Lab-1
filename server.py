import socket
import os
import utilities
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket created successfully")

serverPort = 8080
hostAddress= '127.0.0.1'
serverSocket.bind((hostAddress,serverPort))
print(f"Socket {hostAddress}:{serverPort}")

serverSocket.listen(5)

while True:
    connSocket, addr = serverSocket.accept()
    print(f"Client {addr}")
    connSocket.settimeout(10)
    try:
        http_message = connSocket.recv(1024) #bytes var
        if utilities.server_http_parser(http_message) == 0:
            connSocket.send()
    except IOError:
        print("No access to file!")
    connSocket.close()
    break
serverSocket.close()
