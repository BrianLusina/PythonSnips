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


def validate_ipv4(ip: str) -> str:
    nums = ip.split(".")

    for x in nums:
        # validate integer in range 0-255
        # 1. length of chunk is between 1 and 3
        if len(x) == 0 or len(x) > 3:
            return "Neither"

        # 2. no extra leading zeros
        # 3. only digits are allowed
        # 4. less than 255
        if x[0] == '0' and len(x) != 1 or not x.isdigit() or int(x) > 255:
            return "Neither"
    return "IPv4"


def validate_ipv6(ip: str) -> str:
    nums = ip.split(":")

    hexdigits = "0123456789abcdefABCDEF"

    for x in nums:
        # Validate hexadecimal in range (0, 2**16)
        # 1. at least one and not more than 4 hexdigits in one chunk
        # 2. only hexdigits are allowed: 0-9, a-f, A-F
        if len(x) == 0 or len(x) > 4 or not all(c in hexdigits for c in x):
            return "Neither"
    return "IPv6"


def validate_ip_address_div_conquer(ip: str) -> str:
    """
    Validates an IP address as either IPv4 or IPv6 or returns Neither if the IP is invalid. This splits up the string
    using either . or : and validates the chunks. an IP is only valid if each chunk is valid.
    Space Complexity is O(1)
    Time Complexity is O(n) because to count the number of dots requires parsing the whole input string
    """

    if ip.count(".") == 3:
        return validate_ipv4(ip)
    elif ip.count(":") == 7:
        return validate_ipv6(ip)
    else:
        return "Neither"
