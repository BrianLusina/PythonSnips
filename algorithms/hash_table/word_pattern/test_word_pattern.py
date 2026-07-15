import unittest
from parameterized import parameterized
from utils.test_utils import custom_test_name_func
from algorithms.hash_table.word_pattern import word_pattern, word_pattern_2

WORD_PATTERN_TEST_CASES = [
    ("abba", "dog cat cat dog", True),
    ("abba", "dog dog dog dog", False),
    ("abba", "dog cat cat fish", False),
    ("aaaa", "dog cat cat dog", False),
    ("abc", "red blue green", True),
    ("abcba", "sun moon star moon sun", True),
]


class WordPatternTestCase(unittest.TestCase):
    @parameterized.expand(WORD_PATTERN_TEST_CASES, name_func=custom_test_name_func)
    def test_word_pattern(self, pattern: str, s: str, expected: bool):
        actual = word_pattern(pattern, s)
        self.assertEqual(expected, actual)

    @parameterized.expand(WORD_PATTERN_TEST_CASES, name_func=custom_test_name_func)
    def test_word_pattern_2(self, pattern: str, s: str, expected: bool):
        actual = word_pattern_2(pattern, s)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
