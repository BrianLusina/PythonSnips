import unittest
from typing import List
from parameterized import parameterized
from algorithms.graphs.min_cost_to_supply import (
    min_cost_to_supply_water,
    min_cost_to_supply_water_2,
)

MIN_COST_TO_SUPPLY_WATER_TEST_CASES = [
    (2, [3, 4], [[1, 2, 2]], 5),
    (4, [1, 1, 1, 1], [[1, 2, 1], [2, 3, 1], [3, 4, 1]], 4),
    (3, [10, 10, 1], [[1, 2, 1], [2, 3, 1]], 3),
    (4, [5, 5, 5, 5], [[1, 2, 2], [1, 3, 2], [1, 4, 2]], 11),
    (3, [3, 4, 5], [[1, 2, 5], [2, 3, 6], [1, 3, 7]], 12),
    (3, [8, 2, 3], [[1, 2, 1], [2, 3, 1]], 4),
    (5, [5, 3, 4, 2, 1], [[1, 2, 1], [2, 3, 1], [3, 4, 1], [4, 5, 1]], 5),
    (6, [1, 2, 3, 4, 5, 6], [[1, 2, 1], [2, 3, 1], [3, 4, 1], [4, 5, 1], [5, 6, 1]], 6),
]


class MinCostToSupplyWaterTestCase(unittest.TestCase):
    @parameterized.expand(MIN_COST_TO_SUPPLY_WATER_TEST_CASES)
    def test_min_cost_to_supply_water(
        self, n: int, wells: List[int], pipes: List[List[int]], expected: int
    ):
        actual = min_cost_to_supply_water(n, wells, pipes)
        self.assertEqual(expected, actual)

    @parameterized.expand(MIN_COST_TO_SUPPLY_WATER_TEST_CASES)
    def test_min_cost_to_supply_water_2(
        self, n: int, wells: List[int], pipes: List[List[int]], expected: int
    ):
        actual = min_cost_to_supply_water_2(n, wells, pipes)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
