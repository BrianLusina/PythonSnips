import unittest
import binascii


class HexToDex(object):
    def __init__(self, hex_string):
        self.hex_string = hex_string

    def hex_to_dec(self):
        return int(self.hex_string, 16)

    # alternative version using binascii
    def hex_to_dec_binascii(self):
        return int.from_bytes(binascii.unhexlify(("0" * (len(self.hex_string) % 2)) + self.hex_string), byteorder="big")


class Tests(unittest.TestCase):
    def test_1(self):
        hex_dec = HexToDex("1")
        self.assertEquals(hex_dec.hex_to_dec(), 1)

    def test_2(self):
        hex_dec = HexToDex("a")
        self.assertEquals(hex_dec.hex_to_dec(), 10)

    def test_3(self):
        hex_dec = HexToDex("10")
        self.assertEquals(hex_dec.hex_to_dec(), 16)

    def test_4(self):
        hex_dec = HexToDex("1")
        self.assertEquals(hex_dec.hex_to_dec_binascii(), 1)

    def test_5(self):
        hex_dec = HexToDex("a")
        self.assertEquals(hex_dec.hex_to_dec_binascii(), 10)

    def test_6(self):
        hex_dec = HexToDex("10")
        self.assertEquals(hex_dec.hex_to_dec_binascii(), 16)
