import unittest
from typing import List
from parameterized import parameterized
from algorithms.greedy.spread_stones import minimum_moves


TEST_CASES = [
    ([[0, 0, 1], [1, 0, 4], [1, 1, 1]], 6),
    ([[0, 2, 1], [1, 1, 1], [1, 1, 1]], 1),
    ([[0, 0, 0], [9, 0, 0], [0, 0, 0]], 15),
    ([[6, 0, 0], [1, 0, 0], [1, 0, 1]], 11),
    ([[0, 0, 0], [7, 0, 1], [0, 0, 1]], 10),
]


class MinimumMovesToSpreadStonesTestCase(unittest.TestCase):
    @parameterized.expand(TEST_CASES)
    def test_something(self, grid: List[List[int]], expected: int):
        actual = minimum_moves(grid)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
