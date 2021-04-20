import unittest

from pymath.is_divisible import is_divisible


class IsDivisibleTests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(is_divisible(3, 3, 4), False)

    def test_2(self):
        self.assertEqual(is_divisible(12, 3, 4), True)

    def test_3(self):
        self.assertEqual(is_divisible(8, 3, 4, 2, 5), False)
