import unittest
from typing import List
from parameterized import parameterized
from algorithms.dynamic_programming.maximal_rectangle import (
    maximal_rectangle,
    maximal_rectangle_2,
)

MAXIMAL_RECTANGLE_TEST_CASES = [
    (
        [
            [1, 0, 1, 0, 1],
            [1, 1, 1, 1, 1],
            [0, 1, 1, 1, 0],
            [1, 1, 1, 0, 1],
        ],
        6,
    ),
    (
        [
            [1, 0, 1],
            [1, 1, 1],
            [1, 1, 1],
        ],
        6,
    ),
    (
        [
            [0, 1, 1, 0],
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 0, 0],
        ],
        8,
    ),
    (
        [
            [1, 1, 0, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 0],
        ],
        6,
    ),
    (
        [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
        ],
        0,
    ),
    (
        [
            [1, 0, 1, 1, 1, 0, 1],
        ],
        3,
    ),
    (
        [
            [1, 1, 1],
            [1, 1, 1],
            [1, 1, 1],
        ],
        9,
    ),
    (
        [
            [1, 0, 1],
            [0, 1, 0],
            [1, 0, 1],
        ],
        1,
    ),
    ([[0]], 0),
    ([[1, 0, 1, 0, 0], [1, 0, 1, 1, 1], [1, 1, 1, 1, 1], [1, 0, 0, 1, 0]], 6),
]


class MaximalRectangleTestCase(unittest.TestCase):
    @parameterized.expand(MAXIMAL_RECTANGLE_TEST_CASES)
    def test_maximal_rectangle(self, matrix: List[List[int]], expected: int):
        actual = maximal_rectangle(matrix)
        self.assertEqual(expected, actual)

    @parameterized.expand(MAXIMAL_RECTANGLE_TEST_CASES)
    def test_maximal_rectangle_2(self, matrix: List[List[int]], expected: int):
        actual = maximal_rectangle_2(matrix)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
