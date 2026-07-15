import unittest
from parameterized import parameterized
from utils.test_utils import custom_test_name_func
from algorithms.dynamic_programming.count_number_of_good_subsequences import (
    count_good_subsequences_with_combinatorics,
)

COUNT_NUMBER_OF_GOOD_SUBSEQUENCES_TEST_CASES = [
    ("ab", 3),
    ("a", 1),
    ("aba", 6),
    ("abbcc", 20),
    ("aabbcc", 33),
]


class CountNumberOfGoodSubsequencesTestCase(unittest.TestCase):
    @parameterized.expand(
        COUNT_NUMBER_OF_GOOD_SUBSEQUENCES_TEST_CASES, name_func=custom_test_name_func
    )
    def test_count_good_subsequences_with_combinatorics(self, s: str, expected: int):
        actual = count_good_subsequences_with_combinatorics(s)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
