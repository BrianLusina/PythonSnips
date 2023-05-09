import unittest

from . import beeramid


class BeeramidTestCases(unittest.TestCase):
    def test_1500_and_2(self):
        """should return 12 from a bonus = 1500 and price per can of 2"""
        bonus = 1500
        price = 2
        expected = 12
        actual = beeramid(bonus=bonus, price=price)

        self.assertEqual(expected, actual)

    def test_5000_and_3(self):
        """should return 16 from a bonus = 5000 and price per can of 3"""
        bonus = 5000
        price = 3
        expected = 16
        actual = beeramid(bonus=bonus, price=price)

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
