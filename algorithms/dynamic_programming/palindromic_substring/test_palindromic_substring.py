import unittest
from parameterized import parameterized
from algorithms.dynamic_programming.palindromic_substring import (
    count_palindromic_substrings,
    count_palindromic_substrings_2,
)

COUNT_PALINDROMIC_SUBSTRINGS_TEST_CASES = [
    ("abc", 3),
    ("aaa", 6),
    ("mnm", 4),
    ("zzz", 6),
    ("cat", 3),
    ("lever", 6),
    ("xyxxyz", 9),
    ("wwwwwwwwww", 55),
    ("tattarrattat", 24),
]


class CountPalindromicSubstringsTestCase(unittest.TestCase):
    @parameterized.expand(COUNT_PALINDROMIC_SUBSTRINGS_TEST_CASES)
    def test_count_palindromic_substrings(self, s: str, expected: int):
        actual = count_palindromic_substrings(s)
        self.assertEqual(expected, actual)

    @parameterized.expand(COUNT_PALINDROMIC_SUBSTRINGS_TEST_CASES)
    def test_count_palindromic_substrings_2(self, s: str, expected: int):
        actual = count_palindromic_substrings_2(s)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
