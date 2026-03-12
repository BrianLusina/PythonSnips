import unittest
from typing import List
from parameterized import parameterized
from algorithms.dynamic_programming.longest_increasing_subsequence import (
    longest_increasing_subsequence,
    find_number_of_lis,
)

LONGEST_INCREASING_SUBSEQUENCE_TEST = [
    ([1, 2, 1, 5], 3),
    ([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15], 6),
    ([3, 10, 2, 1, 20], 3),
    ([3, 2], 1),
    ([50, 3, 10, 7, 40, 80], 4),
    ([10, 9, 2, 5, 3, 7, 101, 18], 4),
    ([0, 1, 0, 3, 2, 3], 4),
    ([7, 7, 7, 7, 7, 7, 7], 1),
]

FIND_NUMBER_OF_LONGEST_INCREASING_SUBSEQUENCE_TEST_CASES = [
    ([1, 3, 5, 4, 7], 2),
    ([2, 2, 2, 2, 2], 5),
]


class LongestIncreasingSubsequenceTestCase(unittest.TestCase):
    @parameterized.expand(LONGEST_INCREASING_SUBSEQUENCE_TEST)
    def test_longest_increasing_subsequence(self, nums: List[int], expected: int):
        actual = longest_increasing_subsequence(nums)
        self.assertEqual(expected, actual)

    @parameterized.expand(FIND_NUMBER_OF_LONGEST_INCREASING_SUBSEQUENCE_TEST_CASES)
    def test_find_number_of_lis(self, nums: List[int], expected: int):
        actual = find_number_of_lis(nums)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
