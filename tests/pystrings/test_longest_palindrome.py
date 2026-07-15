import unittest

from algorithms.two_pointers.palindrome import (
    longest_palindrome_one,
    longest_palindrome_two,
)


class LongestPalindromeV1TestCases(unittest.TestCase):
    def test_longest_palindrome_one(self):
        """Should return 7 for s = abccccdd"""
        s = "abccccdd"
        actual = longest_palindrome_one(s)
        expected = 7

        self.assertEqual(expected, actual)

    def test_longest_palindrome_two(self):
        """Should return 1 for s = a"""
        s = "a"
        actual = longest_palindrome_one(s)
        expected = 1

        self.assertEqual(expected, actual)


class LongestPalindromeV2TestCases(unittest.TestCase):
    def test_longest_palindrome_one(self):
        """Should return 7 for s = abccccdd"""
        s = "abccccdd"
        actual = longest_palindrome_two(s)
        expected = 7

        self.assertEqual(expected, actual)

    def test_longest_palindrome_two(self):
        """Should return 1 for s = a"""
        s = "a"
        actual = longest_palindrome_two(s)
        expected = 1

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
