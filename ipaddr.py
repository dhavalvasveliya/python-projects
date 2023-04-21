import ipaddress

def generate_ip_range(cidr_address):
    """
    Generate a range of IP addresses from a CIDR address.
    
    Args:
    - cidr_address (str): CIDR address in the form of "ip_address/subnet_mask".
    
    Returns:
    - ip_range (list): List of IP addresses in the CIDR range.
    """
    
    # Parse the CIDR address
    network = ipaddress.ip_network(cidr_address, strict=False)
    
    # Generate the IP range
    ip_range = [str(ip) for ip in network.hosts()]
    
    return ip_range

cidr_address = "192.168.0.0/27"
ip_range = generate_ip_range(cidr_address)
print(ip_range)
