import unittest
from typing import List
from parameterized import parameterized
from utils.test_utils import custom_test_name_func
from algorithms.dynamic_programming.cherry_pickup import (
    cherry_pickup_dp_top_down,
    cherry_pickup_dp_top_down_2,
    cherry_pickup_dp_bottom_up,
)


CHERRY_PICKUP_TEST_CASES = [
    ([[0, 1, -1], [1, 0, -1], [1, 1, 1]], 5),
    ([[1, 1, -1], [1, -1, 1], [-1, 1, 1]], 0),
    ([[1, 1], [1, 1]], 4),
    ([[0, -1], [1, 1]], 2),
    ([[1]], 1),
    ([[0, 1, 1, 0], [1, -1, 1, 1], [1, 1, -1, 1], [0, 1, 1, 1]], 11),
    ([[1, 1, 0, 0], [-1, 0, -1, 0], [1, 0, -1, 1], [-1, 1, 1, 1]], 6),
    ([[0, 1, 1, 0], [0, -1, 1, -1], [1, 0, -1, 1], [-1, 1, 1, 0]], 3),
    ([[1, 1, 0, 0], [0, -1, 1, -1], [-1, 0, -1, 1], [-1, 1, 0, 0]], 0),
]


class CherryPickupTestCase(unittest.TestCase):
    @parameterized.expand(CHERRY_PICKUP_TEST_CASES, name_func=custom_test_name_func)
    def test_cherry_pickup_dp_top_down(self, grid: List[List[int]], expected: int):
        actual = cherry_pickup_dp_top_down(grid)
        self.assertEqual(expected, actual)

    @parameterized.expand(CHERRY_PICKUP_TEST_CASES, name_func=custom_test_name_func)
    def test_cherry_pickup_dp_top_down_2(self, grid: List[List[int]], expected: int):
        actual = cherry_pickup_dp_top_down_2(grid)
        self.assertEqual(expected, actual)

    @parameterized.expand(CHERRY_PICKUP_TEST_CASES, name_func=custom_test_name_func)
    def test_cherry_pickup_dp_bottom_up(self, grid: List[List[int]], expected: int):
        actual = cherry_pickup_dp_bottom_up(grid)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
