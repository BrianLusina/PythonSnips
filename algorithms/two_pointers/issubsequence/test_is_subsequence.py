import unittest
from parameterized import parameterized
from utils.test_utils import custom_test_name_func
from algorithms.two_pointers.issubsequence import (
    is_subsequence,
    is_subsequence_two_pointers,
)

IS_SUBSEQUENCE_TEST_CASES = [
    ("abc", "ahbgdc", True),
    ("axc", "ahbgdc", False),
    ("", "ahbgdc", True),
    ("b", "abc", True),
]


class IsSubsequenceTestCases(unittest.TestCase):
    @parameterized.expand(IS_SUBSEQUENCE_TEST_CASES, name_func=custom_test_name_func)
    def test_is_subsequence(self, s: str, t: str, expected: bool):
        actual = is_subsequence(s, t)
        self.assertEqual(expected, actual)

    @parameterized.expand(IS_SUBSEQUENCE_TEST_CASES, name_func=custom_test_name_func)
    def test_is_subsequence_two_pointers(self, s: str, t: str, expected: bool):
        actual = is_subsequence_two_pointers(s, t)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
