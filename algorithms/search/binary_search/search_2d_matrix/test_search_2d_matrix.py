import unittest
from typing import List
from parameterized import parameterized
from utils.test_utils import custom_test_name_func
from algorithms.search.binary_search.search_2d_matrix import (
    search_matrix,
    search_matrix_2,
    search_matrix_ii,
    search_matrix_ii_2,
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

SEARCH_2D_MATRIX_II_TEST_CASES = [
    ([[-7, -1, 5, 11], [-6, 0, 6, 14], [-4, 2, 9, 20]], 6, True),
    ([[1, 3, 8], [2, 5, 9], [4, 7, 12]], 6, False),
    ([[-2, 0, 3], [1, 4, 7]], -5, False),
    ([[-10, -3], [-4, 2], [0, 5]], 9, False),
    ([[-13]], -13, True),
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

    @parameterized.expand(
        SEARCH_2D_MATRIX_II_TEST_CASES, name_func=custom_test_name_func
    )
    def test_search_2d_matrix_ii(
        self, matrix: List[List[int]], target: int, expected: bool
    ):
        actual = search_matrix_ii(matrix, target)
        self.assertEqual(expected, actual)

    @parameterized.expand(
        SEARCH_2D_MATRIX_II_TEST_CASES, name_func=custom_test_name_func
    )
    def test_search_2d_matrix_ii_2(
        self, matrix: List[List[int]], target: int, expected: bool
    ):
        actual = search_matrix_ii_2(matrix, target)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
