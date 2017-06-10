import re


def valid_hex_color_code(hex_color):
    """
    checks if a hex color is valid
    :param hex_color: hex color code
    :return: True if color is valid
    """
    r = re.compile('[^\n](#[a-fA-F0-9]{3}(?:[a-fA-F0-9]{3})?)[^a-fA-F0-9]')
    return True if r.match(hex_color) else False
