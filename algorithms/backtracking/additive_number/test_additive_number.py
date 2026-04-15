import unittest
from algorithms.backtracking.additive_number import (
    is_additive_number_dfs,
    is_additive_number_backtrack,
)
from parameterized import parameterized

IS_ADDITIVE_NUMBER_TEST_CASES = [
    ("112358", True),
    ("199100199", True),
    ("11235813", True),
    ("12345", False),
    ("000", True),
    ("1", False),
    ("0", False),
]


class AdditiveNumberTestCase(unittest.TestCase):
    @parameterized.expand(IS_ADDITIVE_NUMBER_TEST_CASES)
    def test_is_additive_number_dfs(self, num: str, expected: bool):
        actual = is_additive_number_dfs(num)
        self.assertEqual(expected, actual)

    @parameterized.expand(IS_ADDITIVE_NUMBER_TEST_CASES)
    def test_is_additive_number_backtrack(self, num: str, expected: bool):
        actual = is_additive_number_backtrack(num)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
