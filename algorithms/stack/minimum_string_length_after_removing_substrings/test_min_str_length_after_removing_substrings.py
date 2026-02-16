import unittest
from parameterized import parameterized
from algorithms.stack.minimum_string_length_after_removing_substrings import (
    min_length_stack,
    min_length_string_replace,
    min_length_in_place_manipulation,
)

MIN_STR_LENGTH_AFTER_REMOVING_SUBSTRINGS_TEST_CASES = [
    ("ABCD", 0),
    ("ACDBD", 1),
    ("ACBD", 4),
    ("ABCDXYZCDAB", 3),
    ("A", 1),
    ("ABFCACDB", 2),
    ("ACBBD", 5),
]


class MinStrLengthAfterRemovingSubstringsTestCase(unittest.TestCase):
    @parameterized.expand(MIN_STR_LENGTH_AFTER_REMOVING_SUBSTRINGS_TEST_CASES)
    def test_min_length(self, s: str, expected: int):
        actual = min_length_stack(s)
        self.assertEqual(expected, actual)

    @parameterized.expand(MIN_STR_LENGTH_AFTER_REMOVING_SUBSTRINGS_TEST_CASES)
    def test_min_length_string_replace(self, s: str, expected: int):
        actual = min_length_string_replace(s)
        self.assertEqual(expected, actual)

    @parameterized.expand(MIN_STR_LENGTH_AFTER_REMOVING_SUBSTRINGS_TEST_CASES)
    def test_min_length_in_place_manipulation(self, s: str, expected: int):
        actual = min_length_in_place_manipulation(s)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
