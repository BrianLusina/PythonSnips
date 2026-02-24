import unittest
from parameterized import parameterized
from algorithms.sliding_window.permutation_in_string import (
    check_inclusion_optimized_sliding_window,
    check_inclusion_sliding_window,
)

PERMUTATION_IN_STRING_TEST_CASES = [
    ("ab", "eidbaooo", True),
    ("ab", "eidboaoo", False),
]


class PermutationInStringTestCase(unittest.TestCase):
    @parameterized.expand(PERMUTATION_IN_STRING_TEST_CASES)
    def test_check_inclusion_optimized_sliding_window(
        self, s1: str, s2: str, expected: bool
    ):
        actual = check_inclusion_optimized_sliding_window(s1, s2)
        self.assertEqual(expected, actual)

    @parameterized.expand(PERMUTATION_IN_STRING_TEST_CASES)
    def test_check_inclusion_sliding_window(self, s1: str, s2: str, expected: bool):
        actual = check_inclusion_sliding_window(s1, s2)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
