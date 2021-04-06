from functools import reduce
from string import hexdigits


class Hexadecimal(object):
    """
    Class for conversion of hexadecimal characters
    initialized with the hexadecimal string
    """

    def __init__(self):
        pass

    @staticmethod
    def hexa_first_principles(hexadecimal):
        """
        Converts a hexadecimal number represented as a string to its decimal equivalent using first principles
        Checks if the input hexadecimal is not in the hexdigits, raises a value error
        :param hexadecimal: string representation of a hexadecimal
        :return: decimal equivalent of hexadecimal
        :rtype: int
        :raises: ValueError
        """
        hexa = hexadecimal.lower()
        if set(hexa) - set(hexdigits[:len(hexdigits) - 6]):
            raise ValueError("Invalid hexadecimal string")

        # if c in hexdigits[10: len(hexdigits) - 6] is equivalent to abcdef
        # converts each character in hexa to digit
        hex_list = [ord(c) - ord('a') + 10 if c in hexdigits[10: len(hexdigits) - 6] else ord(c) - ord('0')
                    for c in hexa]

        # converts each number in the hex_list to base 16
        return reduce(lambda x, y: x * 16 + y, hex_list, 0)

    @staticmethod
    def hex_built_in(hexadecimal):
        """
        Ordinary conversion using built ins
        :return: decimal equivalent of hexadecimal
        """
        return int(hexadecimal, base=16)
