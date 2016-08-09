import unittest


class HexToDex(object):
    def __init__(self, hex_string):
        self.hex_string = hex_string

    def hex_to_dec(self):
        int(self.hex_string, 16)


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
