import unittest

from cryptography.key_press import KeyPress


class Tests(unittest.TestCase):
    def test1(self):
        press = KeyPress("V8")
        self.assertEqual(7, press.presses())

    def test2(self):
        press = KeyPress("LOL")
        self.assertEqual(9, press.presses())

    def test3(self):
        press = KeyPress("How R u 2day")
        self.assertEqual(23, press.presses())

    def test4(self):
        press = KeyPress("i 8 2 Many mandazi 4 brekky")
        self.assertEqual(55, press.presses())
