import unittest
from typing import List
from parameterized import parameterized
from algorithms.intervals.non_overlapping_intervals import erase_overlap_intervals

ERASE_OVERLAP_INTERVALS_TEST_CASES = [
    ([[1, 2], [2, 3], [3, 4], [1, 3]], 1),
    ([[1, 2], [1, 2], [1, 2]], 2),
    ([[1, 2], [2, 3]], 0),
    ([[3, 6], [1, 4], [9, 11], [5, 8]], 1),
    ([[6, 10], [5, 9], [12, 15], [6, 10], [1, 3], [4, 6]], 2),
    ([[1, 2], [2, 4], [3, 6], [5, 10]], 1),
    ([[1, 5], [1, 5], [2, 8], [7, 9], [10, 12]], 2),
    ([[3, 5], [5, 10], [10, 15], [12, 17], [16, 20], [21, 23], [22, 25], [23, 27]], 2),
    ([[4, 8], [8, 14], [15, 17], [16, 17]], 1),
    ([[10, 20], [20, 30], [30, 40], [40, 50], [50, 60]], 0),
]


class NonOverlappingIntervalsTestCase(unittest.TestCase):
    @parameterized.expand(ERASE_OVERLAP_INTERVALS_TEST_CASES)
    def test_erase_non_overlapping_intervals(
        self, intervals: List[List[int]], expected: int
    ):
        actual = erase_overlap_intervals(intervals)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
