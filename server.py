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

def server_http_parser(request: bytes) -> str:
    """
    Parse the GET request for HTMLs

    Args:
        request (bytes): Bit stream HTTP request. DOES NOT ACCEPTS .decode()

    Returns:
        (str): Name of file requested
    """
    message = request.decode().split()
    filename = message[1][1:]
    return filename
def server_http_compiler(filename: str) -> bytes:
    """
    Compile a full HTTP message with the specified HTML file. If filename is "ERROR", a 404 message instead

    Args:
        filename (str): HTML file needed to be compiled to HTTP message

    Returns:
        bytes: Returns a bitstream HTTP message if the filename is found, 404 message otherwise
    """
    try:
        file_content = open(filename, "r").read()
        header = "HTTP/1.1 200 OK\r\n\r\n"
        return (header + file_content).encode()
    except IOError: # Handling file not found or garbage input
        return ("HTTP/1.1 404 Not Found\r\n\r\n" + "<html><body><h1>404 Not Found</h1></body></html>").encode()

while True:
    connSocket, addr = serverSocket.accept()
    print(f"Client {addr}")
    connSocket.settimeout(10)
    http_message = connSocket.recv(1024)
    # Parser gets requested file name and send it straight to compiler
    # File not found is handled by compiler, returning a 404 message
    http_response = server_http_compiler(server_http_parser(http_message))
    connSocket.send(http_response)
    break
serverSocket.close()