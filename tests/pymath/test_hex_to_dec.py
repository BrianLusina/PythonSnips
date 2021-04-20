import unittest

from pymath.binary.hex_to_dec import HexToDex


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
