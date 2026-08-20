import unittest
from typing import List

from parameterized import parameterized
from utils.test_utils import custom_test_name_func
from algorithms.graphs.collect_coins_in_tree import (
    collect_the_coins,
    collect_the_coins_2,
)

COLLECT_COINS_IN_TREE_TEST_CASES = [
    ([1, 0, 0, 0, 0, 1], [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]], 2),
    (
        [0, 0, 0, 1, 1, 0, 0, 1],
        [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [5, 6], [5, 7]],
        2,
    ),
    ([1], [], 0),
    ([0, 0, 0, 0, 0], [[0, 1], [1, 2], [2, 3], [3, 4]], 0),
    (
        [1, 0, 0, 0, 0, 0, 0, 1],
        [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]],
        6,
    ),
    ([0, 1, 1, 1, 1], [[0, 1], [0, 2], [0, 3], [0, 4]], 0),
    ([1, 1], [[0, 1]], 0),
]


class CollectCoinsInTreeTestCase(unittest.TestCase):
    @parameterized.expand(
        COLLECT_COINS_IN_TREE_TEST_CASES, name_func=custom_test_name_func
    )
    def test_collect_the_coins(
        self, coins: List[int], edges: List[List[int]], expected: int
    ):
        actual = collect_the_coins(coins, edges)
        self.assertEqual(expected, actual)

    @parameterized.expand(
        COLLECT_COINS_IN_TREE_TEST_CASES, name_func=custom_test_name_func
    )
    def test_collect_the_coins_2(
        self, coins: List[int], edges: List[List[int]], expected: int
    ):
        actual = collect_the_coins_2(coins, edges)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
