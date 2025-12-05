import unittest
from typing import List
from parameterized import parameterized
from puzzles.arrays.lucky_numbers_in_a_matrix import (
    lucky_numbers,
    lucky_numbers_simulation,
)


class LuckyNumbersInAMatrixTestCase(unittest.TestCase):

    @parameterized.expand(
        [
            ([[3, 7, 8], [9, 11, 13], [15, 16, 17]], [15]),
            ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [7]),
            (
                [
                    [10, 20, 30, 40],
                    [5, 25, 35, 50],
                    [60, 70, 80, 90],
                    [100, 110, 120, 130],
                ],
                [100],
            ),
            (
                [[12, 18, 23, 50], [5, 16, 25, 45], [4, 15, 26, 48], [3, 14, 27, 60]],
                [12],
            ),
            ([[5]], [5]),
            ([[30, 20, 10], [40, 50, 60], [70, 80, 90]], [70]),
            ([[5, 1, 9], [10, 8, 2], [7, 3, 6]], []),
            ([[22, 11], [88, 77], [55, 44]], [77]),
            ([[1, 10, 4, 2], [9, 3, 8, 7], [15, 16, 17, 12]], [12]),
            ([[7, 8], [1, 2]], [7]),
        ]
    )
    def test_lucky_numbers_in_matrix(
        self, matrix: List[List[int]], expected: List[int]
    ):
        actual = lucky_numbers(matrix)
        self.assertEqual(expected, actual)

    @parameterized.expand(
        [
            ([[3, 7, 8], [9, 11, 13], [15, 16, 17]], [15]),
            ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [7]),
            (
                [
                    [10, 20, 30, 40],
                    [5, 25, 35, 50],
                    [60, 70, 80, 90],
                    [100, 110, 120, 130],
                ],
                [100],
            ),
            (
                [[12, 18, 23, 50], [5, 16, 25, 45], [4, 15, 26, 48], [3, 14, 27, 60]],
                [12],
            ),
            ([[5]], [5]),
            ([[30, 20, 10], [40, 50, 60], [70, 80, 90]], [70]),
            ([[5, 1, 9], [10, 8, 2], [7, 3, 6]], []),
            ([[22, 11], [88, 77], [55, 44]], [77]),
            ([[1, 10, 4, 2], [9, 3, 8, 7], [15, 16, 17, 12]], [12]),
            ([[7, 8], [1, 2]], [7]),
        ]
    )
    def test_lucky_numbers_in_matrix_simulation(
        self, matrix: List[List[int]], expected: List[int]
    ):
        actual = lucky_numbers_simulation(matrix)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
