import unittest

from pymath.narcisstic import narcissistic


class NarcissticTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(narcissistic(7), True, '7 is narcissistic')

    def test_2(self):
        self.assertEqual(narcissistic(371), True, '371 is narcissistic')

    def test_3(self):
        self.assertEqual(narcissistic(122), False, '122 is not narcissistic')

    def test_4(self):
        self.assertEqual(narcissistic(4887), False, '4887 is not narcissistic')
