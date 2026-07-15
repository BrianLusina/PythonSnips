import unittest
from parameterized import parameterized
from algorithms.sliding_window.longest_repeating_char_replacement import (
    character_replacement,
    character_replacement_2,
)

LONGEST_REPEATING_CHARACTER_REPLACEMENT_TEST_CASES = [
    ("ABAB", 2, 4),
    ("AABABBA", 1, 4),
    ("AAAA", 1, 4),
    ("ABCDE", 1, 2),
    ("", 2, 0),
    ("", 2, 0),
    ("", 2, 0),
    ("AAABBBCCC", 3, 6),
    ("AABAC", 2, 5),
    ("BAAAB", 2, 5),
    ("aaacbbbaabab", 2, 6),
    ("abbcab", 2, 5),
    ("dippitydip", 4, 6),
    ("coollooc", 2, 6),
    ("aaaaaaaaaa", 2, 10),
    ("lmno", 2, 3),
    ("xxxxx", 1, 5),
    ("fzfzfz", 6, 6),
    ("aabccbb", 2, 5),
    ("BBABCCDD", 2, 5),
]


class LongestRepeatingCharacterReplacementTestCase(unittest.TestCase):
    @parameterized.expand(LONGEST_REPEATING_CHARACTER_REPLACEMENT_TEST_CASES)
    def test_character_replacement(self, s: str, k: int, expected: int):
        actual = character_replacement(s, k)
        self.assertEqual(expected, actual)

    @parameterized.expand(LONGEST_REPEATING_CHARACTER_REPLACEMENT_TEST_CASES)
    def test_character_replacement_2(self, s: str, k: int, expected: int):
        actual = character_replacement_2(s, k)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
