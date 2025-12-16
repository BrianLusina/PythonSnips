import unittest
from typing import List
from parameterized import parameterized
from algorithms.intervals.merge_intervals import merge


class MergeIntervalsTestCase(unittest.TestCase):
    @parameterized.expand(
        [
            ([[10, 12], [12, 15]], [[10, 15]]),
            ([[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]]),
            ([[1, 4], [4, 5]], [[1, 5]]),
            ([[14, 20]], [[14, 20]]),
            ([[1, 5], [4, 6], [3, 7], [6, 8]], [[1, 8]]),
            (
                [[1, 3], [2, 6], [15, 18], [8, 10], [18, 20]],
                [[1, 6], [8, 10], [15, 20]],
            ),
            ([[4, 6], [3, 7], [1, 5]], [[1, 7]]),
            ([[4, 6], [3, 7], [1, 5]], [[1, 7]]),
            ([[1, 5], [4, 6], [11, 15], [6, 8]], [[1, 8], [11, 15]]),
            ([[1, 5]], [[1, 5]]),
            ([[1, 9], [3, 8], [4, 4]], [[1, 9]]),
            ([[1, 2], [8, 8], [3, 4]], [[1, 2], [3, 4], [8, 8]]),
        ]
    )
    def test_merge_intervals(self, intervals: List[List[int]], expected: List[int]):
        actual = merge(intervals)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
