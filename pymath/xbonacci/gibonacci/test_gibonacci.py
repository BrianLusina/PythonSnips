import unittest
from . import gibonacci


class GibonacciTestCase(unittest.TestCase):
    def test_1(self):
        """should return 0 for n=0, x=0, y=1"""
        n = 0
        x = 0
        y = 1
        expected = 0
        actual = gibonacci(n, x, y)
        self.assertEqual(expected, actual)

    def test_2(self):
        """should return 1 for n=1, x=0, y=1"""
        n = 1
        x = 0
        y = 1
        expected = 1
        actual = gibonacci(n, x, y)
        self.assertEqual(expected, actual)

    def test_3(self):
        """should return 1 for n=2, x=0, y=1"""
        n = 2
        x = 0
        y = 1
        expected = 1
        actual = gibonacci(n, x, y)
        self.assertEqual(expected, actual)

    def test_4(self):
        """should return 1 for n=3, x=0, y=1"""
        n = 3
        x = 0
        y = 1
        expected = 0
        actual = gibonacci(n, x, y)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
