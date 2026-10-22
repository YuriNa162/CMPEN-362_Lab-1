def server_http_parser(request: bytes) -> str:
    """
    Parse the GET request for HTMLs

    Args:
        request (bytes): Bit stream HTTP request. DOES NOT ACCEPTS .decode()

    Returns:
        (int): 0 if GET request is index.html, -1 otherwise
    """
    message = request.decode().split()
    filename = message[1][1:]
    if filename[-4:] == "html": # Make sure it's a HTML file
        return filename
    else:
        return "ERROR"
def server_http_compiler(filename: str) -> bytes:
    """
    Compile a full HTTP message with the specified HTML file. If filename is "ERROR", a 404 message instead

    Args:
        filename (str): _description_

    Returns:
        bytes: _description_
    """
    if filename == "ERROR":
        return ("HTTP/1.1 404 Not Found\r\n\r\n" + "<html><body><h1>404 Not Found</h1></body></html>").encode()
    else:
        header = "HTTP/1.1 200 OK\r\n\r\n"
        file_content = open(filename, "r").read()
        return (header + file_content).encode()
    
