import socket
import requests
import re

# Function to check for open ports
def check_open_ports(target_host, target_ports):
    for port in target_ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target_host, port))
        if result == 0:
            print(f"Port {port} is open")
        sock.close()

# Function to check for outdated software versions
def check_outdated_versions(target_url):
    response = requests.get(target_url)
    if response.status_code == 200:
        html_content = response.text
        version_numbers = re.findall(r'Version (\d+\.\d+\.\d+)', html_content)
        if version_numbers:
            print(f"Outdated software versions detected: {', '.join(version_numbers)}")

# Main function
def vulnerability_scanner(target_host, target_ports, target_url):
    print(f"Scanning host {target_host}...")
    check_open_ports(target_host, target_ports)

    if target_url:
        print(f"Scanning URL {target_url}...")
        check_outdated_versions(target_url)

    print("Scan complete.")

# Usage example
if __name__ == '__main__':
    target_host = "example.com"  # Target host or IP address
    target_ports = [80, 443]  # Target ports to scan
    target_url = "http://example.com"  # Target URL for software version scanning

    vulnerability_scanner(target_host, target_ports, target_url)
