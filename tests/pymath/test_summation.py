import unittest

from pymath.summation import summation


class SummationTests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(summation(10), 55)

    def test_2(self):
        self.assertEqual(summation(5), 15)

    def test_3(self):
        self.assertEqual(summation("538"), "Error 404")

    def test_4(self):
        self.assertEqual(summation(67.9), "Error 404")
