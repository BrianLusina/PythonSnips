import unittest
from typing import List
from parameterized import parameterized
from algorithms.dynamic_programming.maximal_square import maximal_square

MAXIMAL_SQUARE_TEST_CASES = [
    (
        [
            [1, 0, 1, 0, 0],
            [1, 0, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 0, 0, 1, 0],
        ],
        4,
    ),
    ([[0, 1], [1, 0]], 1),
    ([[0]], 0),
]


class MaximalSquareTestCase(unittest.TestCase):
    @parameterized.expand(MAXIMAL_SQUARE_TEST_CASES)
    def test_maximal_square(self, matrix: List[List[int]], expected: int):
        actual = maximal_square(matrix)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
