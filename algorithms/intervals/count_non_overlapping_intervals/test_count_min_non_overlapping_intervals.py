import unittest
from typing import List
from copy import deepcopy
from parameterized import parameterized
from algorithms.intervals.count_non_overlapping_intervals import (
    count_min_non_overlapping_intervals,
    count_min_non_overlapping_intervals_2,
)

COUNT_NON_OVERLAPPING_INTERVALS_TEST_CASES = [
    ([[1, 3], [5, 8], [4, 10], [11, 13]], 1),
    ([[1, 2], [2, 3], [3, 4], [1, 3]], 1),
    ([[1, 2], [1, 2], [1, 2]], 2),
    ([[1, 2], [2, 3]], 0),
    ([[1, 5], [2, 3], [3, 4], [4, 6]], 1),
    ([[1, 3], [3, 5], [4, 6], [5, 7]], 1),
    ([[1, 3], [2, 4], [3, 5]], 1),
    ([[0, 2], [1, 3], [2, 4], [3, 5], [4, 6]], 2),
]


class CountMinNonOverlappingIntervalsTestCase(unittest.TestCase):
    @parameterized.expand(COUNT_NON_OVERLAPPING_INTERVALS_TEST_CASES)
    def test_count_non_overlapping_intervals_1(
        self, intervals: List[List[int]], expected: int
    ):
        input_intervals = deepcopy(intervals)
        actual = count_min_non_overlapping_intervals(input_intervals)
        self.assertEqual(expected, actual)

    @parameterized.expand(COUNT_NON_OVERLAPPING_INTERVALS_TEST_CASES)
    def test_count_non_overlapping_intervals_2(
        self, intervals: List[List[int]], expected: int
    ):
        actual = count_min_non_overlapping_intervals_2(intervals)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
