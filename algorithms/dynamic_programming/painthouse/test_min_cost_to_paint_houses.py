import unittest
from typing import List
from parameterized import parameterized
from algorithms.dynamic_programming.painthouse import (
    min_cost_to_paint_houses_alternate_colors,
)

MIN_COST_PAINT_HOUSE = [
    ([[8, 4, 15], [10, 7, 3], [6, 9, 12]], 13),
    ([[5, 8, 6], [19, 14, 13], [7, 5, 12], [14, 5, 9]], 30),
]


class MinCostToPaintHouseTestCase(unittest.TestCase):
    @parameterized.expand(MIN_COST_PAINT_HOUSE)
    def test_min_cost_to_paint_houses(self, cost: List[List[int]], expected: int):
        actual = min_cost_to_paint_houses_alternate_colors(cost)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
