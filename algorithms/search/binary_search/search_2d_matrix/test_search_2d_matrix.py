import unittest
from typing import List
from parameterized import parameterized
from utils.test_utils import custom_test_name_func
from algorithms.search.binary_search.search_2d_matrix import (
    search_matrix,
    search_matrix_2,
)

SEARCH_2D_MATRIX_TEST_CASES = [
    ([[-8, -3, 1, 4], [7, 9, 13, 18], [21, 26, 31, 40]], 13, True),
    ([[-6]], 5, False),
    ([[-5, -2, 0], [3, 6, 10]], -9, False),
    ([[-10, -4, 2, 9, 15, 22]], 9, True),
    ([[-9], [-1], [5], [12], [20]], 6, False),
    ([[0]], 0, True),
    ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3, True),
    ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13, False),
]


class Search2DMatrixTestCase(unittest.TestCase):
    @parameterized.expand(SEARCH_2D_MATRIX_TEST_CASES, name_func=custom_test_name_func)
    def test_search_2d_matrix(
        self, matrix: List[List[int]], target: int, expected: bool
    ):
        actual = search_matrix(matrix, target)
        self.assertEqual(expected, actual)

    @parameterized.expand(SEARCH_2D_MATRIX_TEST_CASES, name_func=custom_test_name_func)
    def test_search_2d_matrix_2(
        self, matrix: List[List[int]], target: int, expected: bool
    ):
        actual = search_matrix_2(matrix, target)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
