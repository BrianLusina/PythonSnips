import unittest
from parameterized import parameterized
from utils.test_utils import custom_test_name_func
from algorithms.hash_table.custom_sort_string import (
    custom_sort_string_custom_comparator,
    custom_sort_string_frequency_table,
)

CUSTOM_SORT_STRING_TEST_CASES = [
    ("cba", "abcd", "cbad"),
    ("bcafg", "abcd", "bcad"),
    ("xyz", "abcdef", "abcdef"),
    ("bca", "xyz", "xyz"),
    ("edcba", "abcde", "edcba"),
    ("wo", "meow", "wome"),
]


class CustomSortStringTestCase(unittest.TestCase):
    @parameterized.expand(
        CUSTOM_SORT_STRING_TEST_CASES, name_func=custom_test_name_func
    )
    def test_custom_sort_string(self, order: str, s: str, expected: str):
        actual = custom_sort_string_custom_comparator(order, s)
        self.assertEqual(expected, actual)

    @parameterized.expand(
        CUSTOM_SORT_STRING_TEST_CASES, name_func=custom_test_name_func
    )
    def test_custom_sort_string_frequency_table(
        self, order: str, s: str, expected: str
    ):
        actual = custom_sort_string_frequency_table(order, s)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
