import unittest
from parameterized import parameterized
from pystrings.integer_to_english import (
    number_to_words_recursion,
    number_to_words_iterative,
    number_to_words_pair,
    number_to_words_recursion_2,
)

INTEGER_TO_ENGLISH_TEST_CASES = [
    (8, "Eight"),
    (50, "Fifty"),
    (948, "Nine Hundred Forty Eight"),
    (10000001, "Ten Million One"),
    (
        2147483647,
        "Two Billion One Hundred Forty Seven Million Four Hundred Eighty Three Thousand Six Hundred Forty Seven",
    ),
    (123, "One Hundred Twenty Three"),
    (1234567, "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"),
]


class IntegerToEnglishTestCases(unittest.TestCase):
    @parameterized.expand(INTEGER_TO_ENGLISH_TEST_CASES)
    def test_integer_to_english_recursion(self, num: int, expected: str):
        actual = number_to_words_recursion(num)
        self.assertEqual(expected, actual)

    @parameterized.expand(INTEGER_TO_ENGLISH_TEST_CASES)
    def test_integer_to_english_recursion_2(self, num: int, expected: str):
        actual = number_to_words_recursion_2(num)
        self.assertEqual(expected, actual)

    @parameterized.expand(INTEGER_TO_ENGLISH_TEST_CASES)
    def test_integer_to_english_iterative(self, num: int, expected: str):
        actual = number_to_words_iterative(num)
        self.assertEqual(expected, actual)

    @parameterized.expand(INTEGER_TO_ENGLISH_TEST_CASES)
    def test_integer_to_english_pair(self, num: int, expected: str):
        actual = number_to_words_pair(num)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
