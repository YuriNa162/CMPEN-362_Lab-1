def uri_parser(uri: str) -> dict:
    """
    Parse the Address, Port, and Request from URI

    Args:
        uri (str): input URI as string

    Returns:
        dict: named Dictionary for Address, Port, and Request
    """
    components = uri.split("/") # Parse URI into its components
    ip_port = components[2].split(":") # Split the IP and port
    results = {
        "Address" : ip_port[0],
        "Port" : int(ip_port[1]),
        "Request" : components[3]
    }
    return results

print(uri_parser("http://localhost:8080/false.html"))