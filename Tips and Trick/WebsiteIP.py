import socket

def get_ip_address(domain):
    try:
        ip_address = socket.gethostbyname(domain)
        return ip_address
    except socket.error as e:
        return f"Error: {e}"

# Example usage:
website_domain = "www.codeswithpankaj.com"
ip_address = get_ip_address(website_domain)

print(f"The IP address of {website_domain} is: {ip_address}")
