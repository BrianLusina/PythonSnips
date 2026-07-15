import unittest
from typing import List
from parameterized import parameterized
from algorithms.backtracking.optimal_account_balancing import (
    min_transfers_backtrack,
    min_transfers_dfs,
)

OPTIMAL_ACCOUNT_BALANCING_TEST_CASES = [
    ([[0, 1, 10], [2, 0, 5]], 2),
    ([[0, 1, 10], [1, 0, 1], [1, 2, 5], [2, 0, 5]], 1),
    ([[0, 1, 40], [1, 0, 30], [1, 4, 10], [4, 5, 15], [0, 3, 10]], 3),
    ([[0, 1, 10], [1, 2, 20], [2, 3, 30], [3, 4, 40], [4, 5, 50]], 5),
    ([[0, 1, 10], [1, 2, 20], [2, 3, 30]], 3),
    ([[0, 1, 20], [0, 1, 20], [2, 0, 30], [3, 4, 30], [4, 5, 5]], 4),
    ([[0, 1, 25], [1, 2, 5], [2, 0, 15]], 2),
    ([[0, 2, 5], [1, 2, 10], [1, 0, 30], [0, 1, 25]], 1),
]


class OptimalAccountBalancingTestCase(unittest.TestCase):
    @parameterized.expand(OPTIMAL_ACCOUNT_BALANCING_TEST_CASES)
    def test_min_transfers_backtrack(
        self, transactions: List[List[int]], expected: int
    ):
        actual = min_transfers_backtrack(transactions)
        self.assertEqual(expected, actual)

    @parameterized.expand(OPTIMAL_ACCOUNT_BALANCING_TEST_CASES)
    def test_min_transfers_dfs(self, transactions: List[List[int]], expected: int):
        actual = min_transfers_dfs(transactions)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
