def server_http_parser(request: bytes) -> int:
    """
    Parse the GET request specifically for index.html

    Args:
        request (bytes): Bit stream HTTP request. DOES NOT ACCEPTS .decode()

    Returns:
        (int): 0 if GET request is index.html, -1 otherwise
    """
    message = request.decode().split()
    for i in range(len(message)):
        if message[i] == 'GET' and message[i] == '/index.html':
            return 0 
        else:
            return -1
def server_http_compiler(filename: str) -> bytes:
    """
    Compile a full HTTP message with the specified HTML file. If filename is "ERROR", a 404 message instead

    Args:
        filename (str): _description_

    Returns:
        bytes: _description_
    """
    if filename == "ERROR":
        return ("HTTP/1.1 404 Not Found\r\n\r\n").encode()
    else:
        file_content = open(filename, "r").read()
    
