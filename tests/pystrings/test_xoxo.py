import unittest

from pystrings.xoxo import xoxo, xoxo_reg


class Tests(unittest.TestCase):
    def test1(self):
        self.assertEqual(True, xoxo("hav fun..xoxo"))

    def test2(self):
        self.assertEqual(False, xoxo("6546516541465"))

    def test3(self):
        self.assertEqual(False, xoxo("xooxxxxooxo"))

    def test4(self):
        self.assertEqual(True, xoxo("xoxoxoxoxoxoxo"))

    def test5(self):
        self.assertEqual(False, xoxo_reg("I have no idea what x is"))
