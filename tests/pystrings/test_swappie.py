import unittest

from pystrings.swappie import Swap


class Tests(unittest.TestCase):
    def test(self):
        word = Swap("TEST")
        self.assertEqual("test", word.swappie(), "ALL CAPS")

    def test1(self):
        word = Swap("Hello World")
        self.assertEqual("hELLO wORLD", word.swappie(), )

    def test2(self):
        word = Swap("Hello World")
        self.assertEqual("hELLO wORLD", word.swappie_two())

    def test3(self):
        word = Swap("My name Is Brian")
        self.assertEqual("mY NAME iS bRIAN", word.swappie())

    def test4(self):
        word = Swap("help ME")
        self.assertEqual("HELP me", word.swappie())

    def test5(self):
        word = Swap("lorem IPSON")
        self.assertEqual("LOREM ipson", word.swappie())

    def test6(self):
        word = Swap("meme")
        self.assertEqual("MEME", word.swappie())

    def test7(self):
        word = Swap("")
        self.assertEqual("", word.swappie(), "empty string")

    def test8(self):
        word = Swap("HEBB")
        self.assertEqual("hebb", word.swappie_four())
