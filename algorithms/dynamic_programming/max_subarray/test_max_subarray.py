import unittest
from typing import List
from parameterized import parameterized
from algorithms.dynamic_programming.max_subarray import (
    find_max_sub_array,
    max_sub_array,
)


MAX_SUB_ARRAY_TEST_CASES = [
    ([], 0),
    ([1], 1),
    ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
    ([5, 4, -1, 7, 8], 23),
    ([1, 2, 3, 4, -10], 10),
    ([-2, 1, -3, 4, 1, -1, 2, 1, -3, 4, -2, -5], 8),
    ([-10, 2, 9, 4, -6, -3, 1, 2, 4, -3, 6], 16),
    ([-3, -2, -8, -7, -6, -4, -6, -3], -2),
]


class MaxSubArrayTestCases(unittest.TestCase):
    @parameterized.expand(MAX_SUB_ARRAY_TEST_CASES)
    def test_find_max_sub_array(self, nums: List[int], expected: int):
        actual = find_max_sub_array(nums)
        self.assertEqual(expected, actual)

    @parameterized.expand(MAX_SUB_ARRAY_TEST_CASES)
    def test_max_sub_array(self, nums: List[int], expected: int):
        actual = max_sub_array(nums)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
