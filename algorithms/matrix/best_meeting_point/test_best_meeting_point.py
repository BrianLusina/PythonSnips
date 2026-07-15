import unittest
from typing import List
from parameterized import parameterized
from algorithms.matrix.best_meeting_point import (
    min_total_distance,
    min_total_distance_2,
)

BEST_MEETING_POINT_TEST_CASES = [
    ([[1, 0, 0], [0, 0, 0], [0, 0, 1]], 4),
    ([[1, 1]], 1),
    ([[0, 0, 1], [1, 0, 0], [0, 0, 1]], 4),
]


class BestMeetingPointTestCase(unittest.TestCase):
    @parameterized.expand(BEST_MEETING_POINT_TEST_CASES)
    def test_min_total_distance(self, grid: List[List[int]], expected: int):
        actual = min_total_distance(grid)
        self.assertEqual(expected, actual)

    @parameterized.expand(BEST_MEETING_POINT_TEST_CASES)
    def test_min_total_distance_2(self, grid: List[List[int]], expected: int):
        actual = min_total_distance_2(grid)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
