import unittest
from typing import List
from parameterized import parameterized
from algorithms.matrix.transpose import transpose_matrix

TRANSPOSE_MATRIX_TEST_CASES = [
    (
        [
            [1, 2],
        ],
        [[1], [2]],
    ),
    (
        [
            [1, 2],
            [3, 4],
            [5, 6],
        ],
        [
            [1, 3, 5],
            [2, 4, 6],
        ],
    ),
    (
        [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ],
        [
            [1, 4, 7],
            [2, 5, 8],
            [3, 6, 9],
        ],
    ),
]


class TransposeMatrixTestCase(unittest.TestCase):
    @parameterized.expand(TRANSPOSE_MATRIX_TEST_CASES)
    def test_transpose_matrix(self, matrix: List[List[int]], expected: List[List[int]]):
        actual = transpose_matrix(matrix)
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
