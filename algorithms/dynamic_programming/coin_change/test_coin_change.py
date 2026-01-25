import unittest
from typing import List
from parameterized import parameterized
from algorithms.dynamic_programming.coin_change import (
    find_minimum_coins,
    coin_change,
    coin_change_dp,
)

FIND_MINIMUM_COINS_TEST_CASES = [
    (25, [1, 5, 10, 25, 100], [25]),
    (15, [1, 5, 10, 25, 100], [5, 10]),
    (23, [1, 4, 15, 20, 50], [4, 4, 15]),
    (63, [1, 5, 10, 21, 25], [21, 21, 21]),
    (
        999,
        [1, 2, 5, 10, 20, 50, 100],
        [2, 2, 5, 20, 20, 50, 100, 100, 100, 100, 100, 100, 100, 100, 100],
    ),
    (21, [2, 5, 10, 20, 50], [2, 2, 2, 5, 10]),
    (27, [4, 5], [4, 4, 4, 5, 5, 5]),
    (0, [1, 5, 10, 21, 25], []),
]


class FindMinimumCoinsTest(unittest.TestCase):
    @parameterized.expand(FIND_MINIMUM_COINS_TEST_CASES)
    def test_find_minimum_coins(
        self, total_change: int, coins: List[int], expected: int
    ):
        actual = find_minimum_coins(total_change, coins)
        self.assertEqual(expected, actual)

    def test_error_testing_for_change_smaller_than_smallest_coin(self):
        with self.assertRaisesWithMessage(ValueError):
            find_minimum_coins(3, [5, 10])

    def test_error_if_no_combination_can_add_up_to_target(self):
        with self.assertRaisesWithMessage(ValueError):
            find_minimum_coins(94, [5, 10])

    def test_cannot_find_negative_change_values(self):
        with self.assertRaisesWithMessage(ValueError):
            find_minimum_coins(-5, [1, 2, 5])

    # Utility functions
    def setUp(self):
        try:
            self.assertRaisesRegex
        except AttributeError:
            self.assertRaisesRegex = self.assertRaisesRegexp

    def assertRaisesWithMessage(self, exception):
        return self.assertRaisesRegex(exception, r".+")


COIN_CHANGE_TEST_CASES = [
    ([1, 2, 5], 11, 3),
    ([2], 4, 2),
    ([5], 3, -1),
    ([1, 2, 5], 0, 0),
    ([2, 3, 4, 6, 8], 23, 4),
]


class CoinChangeTest(unittest.TestCase):
    @parameterized.expand(COIN_CHANGE_TEST_CASES)
    def test_coin_change(self, coins: List[int], total: int, expected: int):
        actual = coin_change(coins, total)
        self.assertEqual(expected, actual)

    @parameterized.expand(COIN_CHANGE_TEST_CASES)
    def test_coin_change_dp(self, coins: List[int], total: int, expected: int):
        actual = coin_change_dp(coins, total)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
