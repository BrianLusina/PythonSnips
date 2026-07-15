import unittest
from math import sqrt, floor
from . import sqrt_estimate


class SqrtEstimateTestCases(unittest.TestCase):
    def test_1(self):
        """should return 2 for x = 4"""
        x = 4
        expected = 2
        actual = sqrt_estimate(x)
        self.assertEqual(expected, actual)

    def test_2(self):
        """should return 2 for x = 8"""
        x = 8
        expected = 2
        actual = sqrt_estimate(x)
        self.assertEqual(expected, actual)

    def test_3(self):
        for n in range(2**10):
            expected = floor(sqrt(n))
            actual = sqrt_estimate(n)
            self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
