import unittest
from parameterized import parameterized
from algorithms.dynamic_programming.shortest_common_supersequence import (
    shortest_common_supersequence,
)

TEST_CASES = [
    ("apple", "plejuice", "applejuice"),
    ("educative", "educative", "educative"),
    ("ababa", "babab", "ababab"),
    ("race", "ecar", "racecar"),
    ("ab", "ac", "abc"),
    # ("abcxyz", "axbycz", "abcxxyyz"),
    ("abc", "ab", "abc"),
    ("aab", "azb", "aabz"),
    ("abac", "cab", "aabcc"),
    ("aaaaaaaa", "aaaaaaaa", "aaaaaaaa"),
]


class ShortestCommonSuperSequenceTestCase(unittest.TestCase):
    @parameterized.expand(TEST_CASES)
    def test_shortest_common_supersequence(self, str1: str, str2: str, expected: str):
        actual = shortest_common_supersequence(str1, str2)
        self.assertEqual(sorted(expected), sorted(actual))


if __name__ == "__main__":
    unittest.main()
