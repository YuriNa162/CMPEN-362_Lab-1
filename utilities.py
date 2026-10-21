def server_http_parser(request: bytes):
    message = request.decode().split()
    for i in range(len(message)):
        if message[i] == 'index.html':
            return 0
        else:
            return -1
def server_http_compiler()