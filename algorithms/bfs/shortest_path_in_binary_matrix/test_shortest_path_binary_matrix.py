import unittest
from typing import List
from parameterized import parameterized
from utils.test_utils import custom_test_name_func
from algorithms.bfs.shortest_path_in_binary_matrix import (
    shortest_path_binary_matrix,
    shortest_path_binary_matrix_2,
)

SHORTEST_PATH_BINARY_MATRIX_TEST_CASES = [
    ([[0]], 1),
    ([[0, 1], [1, 0]], 2),
    ([[1, 0], [0, 0]], -1),
    ([[0, 0, 1], [1, 0, 1], [1, 0, 0]], 3),
    ([[0, 0, 1], [1, 0, 1], [1, 0, 0]], 3),
    ([[0, 0, 0], [0, 0, 0], [0, 0, 1]], -1),
    ([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], 4),
    ([[0, 0, 0], [1, 1, 0], [1, 1, 0]], 4),
    ([[1, 0, 0], [1, 1, 0], [1, 1, 0]], -1),
]


class ShortestPathBinaryMatrixTestCase(unittest.TestCase):
    @parameterized.expand(
        SHORTEST_PATH_BINARY_MATRIX_TEST_CASES, name_func=custom_test_name_func
    )
    def test_shortest_path_binary_matrix(self, grid: List[List[int]], expected: int):
        grid_copy = grid[:]
        actual = shortest_path_binary_matrix(grid_copy)
        self.assertEqual(expected, actual)

    @parameterized.expand(
        SHORTEST_PATH_BINARY_MATRIX_TEST_CASES, name_func=custom_test_name_func
    )
    def test_shortest_path_binary_matrix_2(self, grid: List[List[int]], expected: int):
        grid_copy = grid[:]
        actual = shortest_path_binary_matrix_2(grid_copy)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
