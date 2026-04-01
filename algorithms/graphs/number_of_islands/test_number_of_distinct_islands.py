from typing import List
import unittest
from parameterized import parameterized
from algorithms.graphs.number_of_islands import (
    num_of_distinct_islands,
    num_of_distinct_islands_2,
)

NUMBER_OF_DISTINCT_ISLANDS_TEST_CASES = [
    (
        [[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 1, 1], [0, 0, 0, 1, 1]],
        1,
    ),
    (
        [[1, 1, 0, 1, 1], [1, 0, 0, 0, 0], [0, 0, 0, 0, 1], [1, 1, 0, 1, 1]],
        3,
    ),
    (
        [[1, 0, 0, 1], [1, 1, 0, 1], [0, 0, 0, 0], [1, 0, 0, 1], [1, 0, 0, 1]],
        2,
    ),
    (
        [[1, 1, 1], [1, 1, 1], [1, 1, 1]],
        1,
    ),
    (
        [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
        0,
    ),
]


class NumberOfDistinctIslandsTestCase(unittest.TestCase):
    @parameterized.expand(NUMBER_OF_DISTINCT_ISLANDS_TEST_CASES)
    def test_number_of_distinct_islands(self, grid: List[List[int]], expected: int):
        actual = num_of_distinct_islands(grid)
        self.assertEqual(expected, actual)

    @parameterized.expand(NUMBER_OF_DISTINCT_ISLANDS_TEST_CASES)
    def test_number_of_distinct_islands_2(self, grid: List[List[int]], expected: int):
        actual = num_of_distinct_islands_2(grid)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
