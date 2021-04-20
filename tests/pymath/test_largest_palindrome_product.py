import unittest

from pymath.largest_palindrome_product import find_largest_palindrome_product


class LargestPalindromeProductTestCase(unittest.TestCase):
    def test_digit_2(self):
        self.assertEqual(9009, find_largest_palindrome_product(2))

    def test_digit_3(self):
        self.assertEqual(906609, find_largest_palindrome_product(3))


if __name__ == '__main__':
    unittest.main()
