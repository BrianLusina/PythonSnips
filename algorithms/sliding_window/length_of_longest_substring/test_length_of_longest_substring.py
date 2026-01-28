import unittest
from parameterized import parameterized
from algorithms.sliding_window.length_of_longest_substring import (
    length_of_longest_substring,
    length_of_longest_substring_2
)

LENGTH_OF_LONGEST_SUBSTRING = [
    ("abcabcbb", 3),
    ("bbbbb", 1),
    ("pwwkew", 3),
    ("", 0),
    ("substring", 8),
    ("eghghhgg", 3),
    ("aabbcc", 2),
    ("abccba", 3),
]


class LengthOfLongestSubstringTestCase(unittest.TestCase):
    @parameterized.expand(LENGTH_OF_LONGEST_SUBSTRING)
    def test_length_of_longest_substring(self, s: str, expected: int):
        actual = length_of_longest_substring(s)
        self.assertEqual(expected, actual)

    @parameterized.expand(LENGTH_OF_LONGEST_SUBSTRING)
    def test_length_of_longest_substring_2(self, s: str, expected: int):
        actual = length_of_longest_substring_2(s)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
