import socket
import re

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket created successfully")

uri = input('Enter the URI:')

# Parse the Address, Port, and Request from URI

components = uri.split("/") # Parse URI into its components
ip_port = components[2].split(":") # Split the IP and port
results = {
    "Address" : ip_port[0],
    "Port" : int(ip_port[1]),
    "file" : components[3]
}

clientSocket.connect((results["Address"],results["Port"]))

request_message = f"GET /{results['file']} HTTP/1.1\r\nHost: {results['Address']}\r\n\r\n" # Compiling a request message, / is used for GET to avoid SyntaxWarning
clientSocket.send(request_message.encode())

# Receiving HTTP Message
response = b""
while True:
    data = clientSocket.recv(1024)
    if not data:
        break
    response += data
    
# Parsing HTML
message = response.decode()
if message[2] == "404":
    print("404 Not Found")
else:
    match = re.search(r"HTTP/\d\.\d\s+(\d+)\s+.*?\r\n\r\n(.*)", message, re.DOTALL) #Regex parse HTTP response
    if match:
        status_code = match.group(1)  # e.g., "200" or "404"
        body = match.group(2)         # Everything after the blank header line (\r\n\r\n)
        
        plain_text = re.sub(r"<[^>]+>", "", body) # stripping html tag

        print("Status Code:", status_code)
        print("Body:\n" + plain_text)
