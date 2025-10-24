import unittest
from . import integer_square_root


class IntegerSquareRootTestCase(unittest.TestCase):
    def test_1(self):
        """should return 17 for an input of 300"""
        number = 300
        expected = 17
        actual = integer_square_root(number)
        self.assertEqual(expected, actual)

    def test_3(self):
        """should return 3 for an input of 12"""
        number = 12
        expected = 3
        actual = integer_square_root(number)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
