import unittest
from typing import List
from parameterized import parameterized
from algorithms.graphs.min_cost_valid_path import (
    min_cost_dp,
    min_cost_dijkstra,
    min_cost_0_1_bfs,
    min_cost_0_1_bfs_2,
    min_cost_dfs_and_bfs
)

MIN_COST_TO_MAKE_VALID_PATH_IN_GRID_TEST_CASES = [
    ([[1, 1, 1, 1], [2, 2, 2, 2], [1, 1, 1, 1], [2, 2, 2, 2]], 3),
    ([[1, 1, 3], [3, 2, 2], [1, 1, 4]], 0),
    ([[1, 2], [4, 3]], 1),
    ([[4]], 0),
    ([[1, 1], [1, 1]], 1),
    ([[4, 3, 4, 3], [3, 4, 3, 4]], 3),
    ([[1, 1, 3], [2, 2, 3], [1, 1, 4]], 0),
]


class MinCostToMakeValidPathTestCase(unittest.TestCase):
    @parameterized.expand(MIN_COST_TO_MAKE_VALID_PATH_IN_GRID_TEST_CASES)
    def test_min_cost(self, grid: List[List[int]], expected: int):
        actual = min_cost_dp(grid)
        self.assertEqual(expected, actual)

    @parameterized.expand(MIN_COST_TO_MAKE_VALID_PATH_IN_GRID_TEST_CASES)
    def test_min_cost_dijkstra(self, grid: List[List[int]], expected: int):
        actual = min_cost_dijkstra(grid)
        self.assertEqual(expected, actual)

    @parameterized.expand(MIN_COST_TO_MAKE_VALID_PATH_IN_GRID_TEST_CASES)
    def test_min_cost_0_1_bfs(self, grid: List[List[int]], expected: int):
        actual = min_cost_0_1_bfs(grid)
        self.assertEqual(expected, actual)

    @parameterized.expand(MIN_COST_TO_MAKE_VALID_PATH_IN_GRID_TEST_CASES)
    def test_min_cost_0_1_bfs_2(self, grid: List[List[int]], expected: int):
        actual = min_cost_0_1_bfs_2(grid)
        self.assertEqual(expected, actual)

    @parameterized.expand(MIN_COST_TO_MAKE_VALID_PATH_IN_GRID_TEST_CASES)
    def test_min_cost_dfs_and_bfs(self, grid: List[List[int]], expected: int):
        actual = min_cost_dfs_and_bfs(grid)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
