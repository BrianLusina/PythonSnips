import unittest
from typing import List
from parameterized import parameterized
from algorithms.intervals.remove_min_intervals import (
    remove_min_intervals,
    remove_min_intervals_2,
)


REMOVE_MIN_INTERVALS_TEST_CASES = [
    ([[1, 2], [2, 3], [3, 4], [1, 3]], 1),
    ([[1, 2], [1, 2], [1, 2]], 2),
    ([[1, 2], [2, 3]], 0),
]


class RemoveMinIntervalsTestCase(unittest.TestCase):
    @parameterized.expand(REMOVE_MIN_INTERVALS_TEST_CASES)
    def test_remove_min_intervals(self, intervals: List[List[int]], expected: int):
        actual = remove_min_intervals(intervals)
        self.assertEqual(expected, actual)

    @parameterized.expand(REMOVE_MIN_INTERVALS_TEST_CASES)
    def test_remove_min_intervals_2(self, intervals: List[List[int]], expected: int):
        actual = remove_min_intervals_2(intervals)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
