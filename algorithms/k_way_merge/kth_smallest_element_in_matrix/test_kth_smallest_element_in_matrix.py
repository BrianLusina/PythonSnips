import unittest
from typing import List

from parameterized import parameterized
from algorithms.k_way_merge.kth_smallest_element_in_matrix import (
    kth_smallest_in_matrix_with_heap_1,
    kth_smallest_in_matrix_with_heap_2,
)

KTH_SMALLEST_IN_SORTED_MATRIX_TEST_CASES = [
    ([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8, 13),
    ([[-5]], 1, -5),
    ([[2, 6, 8], [3, 7, 10], [5, 8, 11]], 3, 5),
    ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 4, 4),
    ([[1, 4], [2, 5]], 4, 5),
    ([[1, 1, 1], [1, 1, 1], [1, 1, 1]], 5, 1),
    (
        [
            [1, 3, 5, 7, 9],
            [2, 4, 6, 8, 10],
            [11, 13, 15, 17, 19],
            [12, 14, 16, 18, 20],
            [21, 22, 23, 24, 25],
        ],
        11,
        11,
    ),
]


class KthSmallestInMatrixTestCase(unittest.TestCase):
    @parameterized.expand(KTH_SMALLEST_IN_SORTED_MATRIX_TEST_CASES)
    def test_kth_smallest_in_matrix_1(
        self, matrx: List[List[int]], k: int, expected: int
    ):
        actual = kth_smallest_in_matrix_with_heap_1(matrx, k)
        self.assertEqual(expected, actual)

    @parameterized.expand(KTH_SMALLEST_IN_SORTED_MATRIX_TEST_CASES)
    def test_kth_smallest_in_matrix_2(
        self, matrx: List[List[int]], k: int, expected: int
    ):
        actual = kth_smallest_in_matrix_with_heap_2(matrx, k)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
