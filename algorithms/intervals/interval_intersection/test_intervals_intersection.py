import unittest
from typing import List
from parameterized import parameterized
from algorithms.intervals.interval_intersection import intervals_intersection

test_cases = [
    (
        [[1, 4], [5, 6], [7, 8], [9, 15]],
        [[2, 4], [5, 7], [9, 15]],
        [[2, 4], [5, 6], [7, 7], [9, 15]],
    ),
    (
        [[1, 3], [4, 6], [8, 10], [11, 15]],
        [[2, 3], [10, 15]],
        [[2, 3], [10, 10], [11, 15]],
    ),
    (
        [[1, 2], [4, 6], [7, 8], [9, 10]],
        [[3, 6], [7, 8], [9, 10]],
        [[4, 6], [7, 8], [9, 10]],
    ),
    (
        [[1, 3], [5, 6], [7, 8], [9, 10], [12, 15]],
        [[2, 4], [7, 10]],
        [[2, 3], [7, 8], [9, 10]],
    ),
    ([[1, 2]], [[1, 2]], [[1, 2]]),
    ([[3, 9], [20, 31]], [[1, 8], [10, 20], [25, 37]], [[3, 8], [20, 20], [25, 31]]),
    ([[5, 12], [16, 25], [28, 36]], [[0, 40]], [[5, 12], [16, 25], [28, 36]]),
    (
        [[2, 9], [18, 29], [38, 48]],
        [[4, 14], [20, 26], [34, 44]],
        [[4, 9], [20, 26], [38, 44]],
    ),
    (
        [[5, 13], [25, 36]],
        [[13, 25], [40, 50]],
        [[13, 13], [25, 25]],
    ),
    (
        [[1, 12], [29, 38]],
        [[16, 27], [40, 48]],
        [],
    ),
]


class IntervalsIntersectionTestCases(unittest.TestCase):
    @parameterized.expand(test_cases)
    def test_intervals_intersection(
        self,
        interval_list_a: List[List[int]],
        interval_list_b: List[List[int]],
        expected: List[List[int]],
    ):
        actual = intervals_intersection(interval_list_a, interval_list_b)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
