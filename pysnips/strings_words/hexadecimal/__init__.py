from functools import reduce


class Hexadecimal(object):
    """
    Class for conversion of hexadecimal characters
    initialized with the hexadecimal string
    """
    def __init__(self):
        pass

    def hexa_first_principles(self, hexadecimal):
        """
        Converts a hexadecimal number represented as a string to its decimal equivalent using first principles
        :param hexadecimal: string representation of a hexadecimal
        :return: decimal equivalent of hexadecimal
        :rtype: int
        """
        

    def hex_built_in(self, hexadecimal):
        """
        Ordinary conversion using built ins
        :return: decimal equivalent of hexadecimal
        """
        return int(hexadecimal, base=16)

