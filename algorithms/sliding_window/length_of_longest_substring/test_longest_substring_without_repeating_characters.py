import unittest
from parameterized import parameterized
from algorithms.sliding_window.length_of_longest_substring import (
    longest_substring_without_duplication,
)


LONGEST_SUBSTRING_WITHOUT_REPEATING_CHARACTERS = [
    ("clementisacap", "mentisac"),
    ("abcabcbb", "abc"),
    ("bbbbb", "b"),
    ("pwwkew", "wke"),
    ("", ""),
    ("substring", "ubstring"),
    ("eghghhgg", "egh"),
    ("aabbcc", "ab"),
    ("abccba", "abc"),
]


class LongestSubstringWithoutDuplicationTestCase(unittest.TestCase):
    @parameterized.expand(LONGEST_SUBSTRING_WITHOUT_REPEATING_CHARACTERS)
    def test_longest_substring_without_duplication(self, s: str, expected: str):
        actual = longest_substring_without_duplication(s)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
