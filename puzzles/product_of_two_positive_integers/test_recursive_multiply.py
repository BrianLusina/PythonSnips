import unittest
from . import recursive_multiply


class RecursiveMultiplyTestCase(unittest.TestCase):
    def test_1(self):
        """should return 15 from 5 and 3"""
        x = 5
        y = 3
        expected = x*y
        actual = recursive_multiply(x, y)
        self.assertEqual(expected, actual)

    def test_2(self):
        """should return 1000000 from 500 and 2000"""
        x = 500
        y = 2000
        expected = x*y
        actual = recursive_multiply(x, y)
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
