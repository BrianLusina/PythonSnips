import unittest
from typing import List
from parameterized import parameterized
from algorithms.intervals.find_right_interval import (
    find_right_interval_sorting_binary_search,
    find_right_interval_two_heaps,
)

FIND_RIGHT_INTERVAL_TEST_CASES = [
    ([[1, 3], [4, 6], [7, 9], [10, 12]], [1, 2, 3, -1]),
    ([[5, 10], [11, 15], [1, 4]], [1, -1, 0]),
    ([[5, 6], [3, 5], [1, 3]], [-1, 0, 1]),
    ([[2, 3]], [-1]),
    ([[1, 2], [3, 4], [5, 6]], [1, 2, -1]),
    ([[1, 2]], [-1]),
    ([[3, 4], [2, 3], [1, 2]], [-1, 0, 1]),
    ([[1, 4], [2, 3], [3, 4]], [-1, 2, -1]),
]


class FindRightIntervalTestCase(unittest.TestCase):
    @parameterized.expand(FIND_RIGHT_INTERVAL_TEST_CASES)
    def test_find_right_interval(self, intervals: List[List[int]], expected: List[int]):
        actual = find_right_interval_sorting_binary_search(intervals)
        self.assertEqual(actual, expected)

    @parameterized.expand(FIND_RIGHT_INTERVAL_TEST_CASES)
    def test_find_right_interval_two_heaps(
        self, intervals: List[List[int]], expected: List[int]
    ):
        actual = find_right_interval_two_heaps(intervals)
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
