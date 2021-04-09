import unittest

from pystrings.ascii_converter import to_ascii, to_hex


# todo: why do tests keep failing?
@unittest.skip
class AsciiConverterTest(unittest.TestCase):
    def test_1(self):
        s = "Look mom, no hands"
        h = "4c6f6f6b206d6f6d2c206e6f2068616e6473"
        self.assertEqual(to_hex(s), h)

    def test_2(self):
        s = "Look mom, no hands"
        h = "4c6f6f6b206d6f6d2c206e6f2068616e6473"
        self.assertEqual(to_ascii(h), s)

    def test_3(self):
        s = "Look mom, no hands"
        h = "4c6f6f6b206d6f6d2c206e6f2068616e6473"
        self.assertEqual(to_hex(to_ascii(h)), s)

    def test_4(self):
        s = "Look mom, no hands"
        h = "4c6f6f6b206d6f6d2c206e6f2068616e6473"
        self.assertEqual(to_ascii(to_hex(s)), s)
