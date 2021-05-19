import re
from ipaddress import ip_address, IPv6Address


def validate_ip_address(ip: str) -> str:
    """
    Validates real life IP addresses
    """
    try:
        return "IPV6" if type(ip_address(ip)) is IPv6Address else "IPV4"
    except ValueError:
        return "Neither"


def validate_ip_address_regex(ip: str) -> str:
    """
    validates an IP address using REGEX. This will validate where there are leading zeros as is outlined in the problem
    description

    Time complexity: O(1) because the patterns to match have constant length.

    Space complexity: O(1).
    """

    # use 'r' to indicate raw strings, to avoid problems with special characters
    chunk_ipv4 = r'([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'
    pattern_ipv4 = re.compile(r'^(' + chunk_ipv4 + r'\.){3}' + chunk_ipv4 + r'$')

    chunk_ipv6 = r'([0-9a-fA-F]{1,4})'
    pattern_ipv6 = re.compile(r'^(' + chunk_ipv6 + r'\:){7}' + chunk_ipv6 + r'$')

    if pattern_ipv4.match(ip):
        return "IPv4"
    return "IPv6" if pattern_ipv6.match(ip) else "Neither"
