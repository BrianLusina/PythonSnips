import unittest

from pystrings.pattern import pattern


class PatternTests(unittest.TestCase):
    def test1(self):
        self.assertEqual(pattern(1), "1")

    def test2(self):
        self.assertEqual(pattern(2), "1\n1*2")

    def test3(self):
        self.assertEqual(pattern(5), "1\n1*2\n1**3\n1***4\n1****5")

    def test_4(self):
        self.assertEqual(pattern(3), "1\n1*2\n1**3")

    def test_5(self):
        self.assertEqual(pattern(7), "1\n1*2\n1**3\n1***4\n1****5\n1*****6\n1******7")

    def test_6(self):
        self.assertEqual(pattern(20),
                         "1\n1*2\n1**3\n1***4\n1****5\n1*****6\n1******7\n1*******8\n1********9\n1*********10\n1**********11""\n1***********12\n1************13\n1*************14\n1**************15\n1***************16\n1****************17"
                         "\n1*****************18\n1******************19\n1*******************20")
