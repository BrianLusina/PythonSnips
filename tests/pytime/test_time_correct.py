import unittest

from pytime.time_correct import time_correct


class Tests(unittest.TestCase):
    def test2(self):
        self.assertEqual(time_correct(None), None)

    def test3(self):
        self.assertEqual(time_correct(""), "")

    def test4(self):
        self.assertEqual(time_correct("001122"), None)

    def test5(self):
        self.assertEqual(time_correct("00;11;22"), None)

    def test6(self):
        self.assertEqual(time_correct("0a:1c:22"), None)

    def test7(self):
        self.assertEqual(time_correct("09:10:01"), "09:10:01")

    def test8(self):
        self.assertEqual(time_correct("11:70:10"), "12:10:10")

    def test9(self):
        self.assertEqual(time_correct("19:99:99"), "20:40:39")

    def test10(self):
        self.assertEqual(time_correct("24:01:01"), "00:01:01")

    def test11(self):
        self.assertEqual(time_correct("52:01:01"), "04:01:01")
