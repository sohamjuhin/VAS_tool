# VAS_tool
Vulnerability Assessment Scanner Tool
In this code, the check_open_ports() function scans the target host for open ports by attempting to establish a TCP connection to each port in the target_ports list.

The check_outdated_versions() function performs a simple web scraping of the target URL to identify outdated software versions by extracting version numbers using regular expressions.

The vulnerability_scanner() function is the main function that calls the open port and outdated version checks based on the provided target host, ports, and URL.

Remember that this is a basic example, and a complete vulnerability assessment scanner tool requires more comprehensive techniques, including vulnerability databases, exploit checks, and security assessment frameworks. It's recommended to use professional vulnerability assessment tools or libraries for thorough assessments.
