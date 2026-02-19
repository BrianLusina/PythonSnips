import unittest
import copy
from typing import List
from parameterized import parameterized
from algorithms.dynamic_programming.min_path_sum import min_path_sum_in_triangle, min_path_sum_in_triangle_2, min_path_sum_grid, min_path_sum_grid_2

MIN_PATH_SUM_TRIANGLE_TEST_CASES = [
    ([[5]], 5),
    ([[2], [3, 4]], 5),
    ([[1000], [2000, 3000]], 3000),
    ([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]], 11),
    ([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]], 17),
]

MIN_PATH_SUM_GRID_TEST_CASES = [
    ([[1,3,1],[1,5,1],[4,2,1]], 7),
    ([[1,2,3],[4,5,6]], 12),
    ([[1, 2, 5], [3, 2, 1]], 6),
    ([[5, 9, 1, 3], [4, 2, 1, 7], [3, 1, 1, 2]], 15),
    ([[5]], 5),
    ([[1, 0, 0], [1, 1, 0], [1, 1, 1]], 2),
    ([[7, 1, 3, 2], [2, 5, 10, 1], [4, 2, 1, 3]], 17),
]


class MinPathSumTestCase(unittest.TestCase):
    @parameterized.expand(MIN_PATH_SUM_TRIANGLE_TEST_CASES)
    def test_min_path_sum_in_triangle(self, triangle: List[List[int]], expected: int):
        input_triangle = copy.deepcopy(triangle)
        actual = min_path_sum_in_triangle(input_triangle)
        self.assertEqual(expected, actual)

    @parameterized.expand(MIN_PATH_SUM_TRIANGLE_TEST_CASES)
    def test_min_path_sum_2_in_triangle(self, triangle: List[List[int]], expected: int):
        input_triangle = copy.deepcopy(triangle)
        actual = min_path_sum_in_triangle_2(input_triangle)
        self.assertEqual(expected, actual)

    @parameterized.expand(MIN_PATH_SUM_GRID_TEST_CASES)
    def test_min_path_sum_in_grid(self, grid: List[List[int]], expected: int):
        input_triangle = copy.deepcopy(grid)
        actual = min_path_sum_grid(input_triangle)
        self.assertEqual(expected, actual)

    @parameterized.expand(MIN_PATH_SUM_GRID_TEST_CASES)
    def test_min_path_sum_2_in_grid(self, grid: List[List[int]], expected: int):
        input_triangle = copy.deepcopy(grid)
        actual = min_path_sum_grid_2(input_triangle)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
