import unittest
from parameterized import parameterized
from algorithms.dynamic_programming.interleaving_string import (
    is_interleave_dp_top_down,
    is_interleave_dp_bottom_up,
)


IS_INTERLEAVE_TEST_CASES = [
    ("aabcc", "dbbca", "aadbbcbcac", True),
    ("aabcc", "dbbca", "aadbbbaccc", False),
    ("", "", "", True),
    ("abc", "def", "adbcef", True),
    ("", "abc", "abc", True),
    ("xx", "yy", "xyxy", True),
]


class IsInterleaveTestCase(unittest.TestCase):
    @parameterized.expand(IS_INTERLEAVE_TEST_CASES)
    def test_is_interleave_dp_top_down(self, s1: str, s2: str, s3: str, expected: bool):
        actual = is_interleave_dp_top_down(s1, s2, s3)
        self.assertEqual(expected, actual)

    @parameterized.expand(IS_INTERLEAVE_TEST_CASES)
    def test_is_interleave_dp_bottom_up(
        self, s1: str, s2: str, s3: str, expected: bool
    ):
        actual = is_interleave_dp_bottom_up(s1, s2, s3)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
