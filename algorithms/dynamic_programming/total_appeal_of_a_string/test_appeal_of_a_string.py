import unittest
from parameterized import parameterized
from algorithms.dynamic_programming.total_appeal_of_a_string import (
    appeal_sum_dp,
    appeal_sum_hash_table,
)

APPEAL_SUM_TEST_CASES = [
    ("abbca", 28),
    ("code", 20),
    ("asd", 10),
    ("bbb", 6),
    ("q", 1),
    ("madam", 30),
    ("hippopotamus", 279),
]


class AppealSumTestCase(unittest.TestCase):
    @parameterized.expand(APPEAL_SUM_TEST_CASES)
    def test_appeal_sum_dp(self, s: str, expected: int):
        actual = appeal_sum_dp(s)
        self.assertEqual(expected, actual)

    @parameterized.expand(APPEAL_SUM_TEST_CASES)
    def test_appeal_sum_hash_table(self, s: str, expected: int):
        actual = appeal_sum_hash_table(s)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
