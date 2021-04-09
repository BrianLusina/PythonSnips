import unittest

from pystrings.uni_total import uni_total


class UniTotalTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(uni_total("a"), 97)

    def test_2(self):
        self.assertEqual(uni_total("b"), 98)

    def test_3(self):
        self.assertEqual(uni_total("c"), 99)

    def test_4(self):
        self.assertEqual(uni_total(""), 0)

    def test_5(self):
        self.assertEqual(uni_total("aaa"), 291)

    def test_6(self):
        self.assertEqual(uni_total("abc"), 294)

    def test_7(self):
        self.assertEqual(uni_total("Mary Had A Little Lamb"), 1873)

    def test_8(self):
        self.assertEqual(uni_total("Mary had a little lamb"), 2001)

    def test_9(self):
        self.assertEqual(uni_total("CodeWars rocks"), 1370)

    def test(self):
        self.assertEqual(uni_total("And so does Strive"), 1661)
