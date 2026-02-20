import unittest
from typing import List
from parameterized import parameterized
from algorithms.intervals.min_intervals_for_queries import min_interval

MIN_INTERVAL_TO_INCLUDE_QUERY_TEST_CASES = [
    ([[1, 4], [2, 4], [3, 6], [4, 4]], [2, 3, 4, 5], [3, 3, 1, 4]),
    ([[2, 3], [2, 5], [1, 8], [20, 25]], [2, 19, 5, 22], [2, -1, 4, 6]),
    ([[1, 3], [2, 6], [8, 10], [9, 9]], [1, 2, 4, 9, 10, 7], [3, 3, 5, 1, 3, -1]),
    ([[4, 4], [2, 5], [1, 7], [6, 8]], [4, 5, 6, 1, 8, 9], [1, 4, 3, 7, 3, -1]),
    (
        [[10, 20], [1, 2], [3, 5], [6, 9], [2, 12]],
        [2, 4, 6, 10, 12, 21],
        [2, 3, 4, 11, 11, -1],
    ),
]


class MinIntervalForQueryTestCase(unittest.TestCase):
    @parameterized.expand(MIN_INTERVAL_TO_INCLUDE_QUERY_TEST_CASES)
    def test_min_interval(
        self, intervals: List[List[int]], queries: List[int], expected: List[int]
    ):
        actual = min_interval(intervals, queries)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
