import unittest
import binascii


class HexToDex(object):
    def __init__(self, hex_string):
        self.hex_string = hex_string

    def hex_to_dec(self):
        int(self.hex_string, 16)

    # alternative version using binascii
    def hex_to_dec_binascii(self):
        return int.from_bytes(binascii.unhexlify(("0" * (len(s) % 2)) + self.hex_string), byteorder="big")


class Tests(unittest.TestCase):
    def test_1(self):
        hexDec = HexToDex("1")
        self.assertEquals(hexDec.hex_to_dec(), 1)

    def test_2(self):
        hexDec = HexToDex("a")
        self.assertEquals(hexDec.hex_to_dec(), 10)

    def test_3(self):
        hexDec = HexToDex("10")
        self.assertEquals(hexDec.hex_to_dec(), 16)

    def test_4(self):
        hexDec = HexToDex("1")
        self.assertEquals(hexDec.hex_to_dec_binascii()c(), 1)

    def test_5(self):
        hexDec = HexToDex("a")
        self.assertEquals(hexDec.hex_to_dec_binascii()c(), 10)

    def test_6(self):
        hexDec = HexToDex("10")
        self.assertEquals(hexDec.hex_to_dec_binascii()ec(), 16)
