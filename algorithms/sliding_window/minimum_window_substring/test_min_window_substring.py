import unittest
from parameterized import parameterized
from algorithms.sliding_window.minimum_window_substring import min_window, min_window_2

MIN_WINDOW_SUBSTRING_TEST_CASES = [
    ("ADOBECODEBANC", "ABC", "BANC"),
    ("a", "a", "a"),
    ("a", "aa", ""),
    ("ABCD", "ABC", "ABC"),
    ("XYZYX", "XYZ", "XYZ"),
    ("ABXYZJKLSNFC", "ABC", "ABXYZJKLSNFC"),
    ("AAAAAAAAAAA", "A", "A"),
    ("ABDFGDCKAB", "ABCD", "DCKAB"),
]


class MinWindowSubstringTestCase(unittest.TestCase):
    @parameterized.expand(MIN_WINDOW_SUBSTRING_TEST_CASES)
    def test_min_window_substring(self, s: str, t: str, expected: str):
        actual = min_window(s, t)
        self.assertEqual(expected, actual)

    @parameterized.expand(MIN_WINDOW_SUBSTRING_TEST_CASES)
    def test_min_window_substring_2(self, s: str, t: str, expected: str):
        actual = min_window_2(s, t)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
