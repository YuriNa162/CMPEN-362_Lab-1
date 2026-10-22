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