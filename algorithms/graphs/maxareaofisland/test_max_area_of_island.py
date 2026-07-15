import unittest
from typing import List
from parameterized import parameterized
from utils.test_utils import custom_test_name_func
from algorithms.graphs.maxareaofisland import (
    max_area_of_island,
    max_area_of_island_iterative,
)

MAX_AREA_OF_ISLAND_TEST_CASES = [
    ([[]], 0),
    ([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], 0),
    (
        [
            [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
        ],
        6,
    ),
    ([[1, 1, 0], [0, 1, 0], [0, 0, 1]], 3),
    ([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], 0),
    ([[1, 1, 1, 1, 1], [1, 1, 1, 1, 1]], 10),
    ([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]], 1),
    (
        [
            [0, 1, 1, 0, 0, 0],
            [0, 1, 1, 1, 0, 0],
            [0, 0, 0, 1, 1, 1],
            [1, 0, 0, 0, 0, 1],
        ],
        9,
    ),
]


class TestMaxAreaOfIsland(unittest.TestCase):
    @parameterized.expand(
        MAX_AREA_OF_ISLAND_TEST_CASES, name_func=custom_test_name_func
    )
    def test_max_area_of_island_recursive(self, grid: List[List[int]], expected: int):
        """should return 0 for empty grid"""
        actual = max_area_of_island(grid)
        self.assertEqual(actual, expected)

    @parameterized.expand(MAX_AREA_OF_ISLAND_TEST_CASES)
    def test_max_area_of_island_iterative(self, grid: List[List[int]], expected: int):
        actual = max_area_of_island_iterative(grid)
        self.assertEqual(actual, expected)

    # def test_grid_with_no_islands(self):
    #     """should return 0 for grid with no islands"""
    #     grid = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    #     expected = 0
    #     actual = max_area_of_island(grid)
    #     self.assertEqual(expected, actual)
    #
    # def test_should_return_max_area_of_island(self):
    #     grid = [
    #         [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    #         [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    #         [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
    #         [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
    #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    #         [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    #         [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    #     ]
    #     expected = 6
    #     actual = max_area_of_island(grid)
    #     self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
