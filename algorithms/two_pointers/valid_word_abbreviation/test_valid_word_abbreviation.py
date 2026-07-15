import unittest
from parameterized import parameterized
from algorithms.two_pointers.valid_word_abbreviation import (
    valid_word_abbreviation,
    valid_word_abbreviation_2,
)


VALID_WORD_ABBREVIATION_TEST_CASES = [
    ("internationalization", "13iz4n", True),
    ("helloworld", "4orworld", False),
    ("minimum", "min2um", True),
    ("subsequences", "3sequ3es", True),
    ("computation", "compu03on", False),
]


class ValidWordAbbreviationTestCase(unittest.TestCase):
    @parameterized.expand(VALID_WORD_ABBREVIATION_TEST_CASES)
    def test_valid_word_abbreviation(self, word: str, abbr: str, expected: bool):
        actual = valid_word_abbreviation(word, abbr)
        self.assertEqual(expected, actual)

    @parameterized.expand(VALID_WORD_ABBREVIATION_TEST_CASES)
    def test_valid_word_abbreviation_2(self, word: str, abbr: str, expected: bool):
        actual = valid_word_abbreviation_2(word, abbr)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
