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
    http_message = connSocket.recv(1024)
    # Parser gets requested file name and send it straight to compiler
    # File not found is handled by compiler, returning a 404 message
    http_response = utilities.server_http_compiler(utilities.server_http_parser(http_message))
    connSocket.send(http_response)
    break
serverSocket.close()
