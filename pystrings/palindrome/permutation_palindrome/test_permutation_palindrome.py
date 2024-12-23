import unittest
from . import has_palindrome_permutation, is_palindrome_permutation


class HasPalindromePermutationTestCases(unittest.TestCase):
    def test_1(self):
        """should return true for 'Tact Coa'"""
        s = "Tact Coa"
        actual = has_palindrome_permutation(s)
        self.assertTrue(actual)

    def test_2(self):
        """should return true for 'This is not a palindrome permutation'"""
        s = "This is not a palindrome permutation"
        actual = has_palindrome_permutation(s)
        self.assertFalse(actual)

    def test_3(self):
        """should return true for 'taco cat'"""
        s = "taco cat"
        actual = has_palindrome_permutation(s)
        self.assertTrue(actual)


class IsPalindromePermutationTestCases(unittest.TestCase):
    def test_1(self):
        """should return true for 'Tact Coa'"""
        s = "Tact Coa"
        actual = is_palindrome_permutation(s)
        self.assertTrue(actual)

    def test_2(self):
        """should return true for 'This is not a palindrome permutation'"""
        s = "This is not a palindrome permutation"
        actual = is_palindrome_permutation(s)
        self.assertFalse(actual)

    def test_3(self):
        """should return true for 'taco cat'"""
        s = "taco cat"
        actual = is_palindrome_permutation(s)
        self.assertTrue(actual)


if __name__ == '__main__':
    unittest.main()
