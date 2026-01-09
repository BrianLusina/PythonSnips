import unittest
from parameterized import parameterized
from algorithms.two_pointers.reverse_words import (
    reverse_words,
    reverse_words_two_pointers,
)

REVERSE_WORDS_TEST_CASES = [
    ("vault", "vault"),
    ("thief cake", "cake thief"),
    ("one another get", "get another one"),
    ("rat the ate cat the", "the cat ate the rat"),
    ("yummy is cake bundt chocolate", "chocolate bundt cake is yummy"),
    ("", ""),
    ("  hello world  ", "world hello"),
    ("a good   example", "example good a"),
    ("We love Python ", "Python love We"),
    ("1234 abc XYZ", "XYZ abc 1234"),
    ("You are amazing", "amazing are You"),
    ("Hello     World", "World Hello"),
    ("   Greeting123   ", "Greeting123"),
]


class ReverseWordsTests(unittest.TestCase):
    @parameterized.expand(REVERSE_WORDS_TEST_CASES)
    def test_reverse_words(self, message: str, expected: str):
        actual = reverse_words(message)
        self.assertEqual(expected, actual)

    @parameterized.expand(REVERSE_WORDS_TEST_CASES)
    def test_reverse_words_two_pointers(self, message: str, expected: str):
        actual = reverse_words_two_pointers(message)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
