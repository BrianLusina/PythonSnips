import unittest
from parameterized import parameterized
from algorithms.dynamic_programming.palindromic_substring.longest_palindromic_substring import (
    longest_palindromic_substring,
)

LONGEST_PALINDROMIC_SUBSTRING_TEST_CASES = [
    ("", ""),
    ("a", "a"),
    ("aab", "aa"),
    ("baa", "aa"),
    ("mnm", "mnm"),
    ("zzz", "zzz"),
    ("cat", "c"),
    ("lever", "eve"),
    ("xyxxyz", "yxxy"),
    ("wwwwwwwwww", "wwwwwwwwww"),
    ("tattarrattat", "tattarrattat"),
]


class LongestPalindromicSubstringTestCase(unittest.TestCase):
    @parameterized.expand(LONGEST_PALINDROMIC_SUBSTRING_TEST_CASES)
    def test_longest_palindromic_substrings(self, s: str, expected: str):
        actual = longest_palindromic_substring(s)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
