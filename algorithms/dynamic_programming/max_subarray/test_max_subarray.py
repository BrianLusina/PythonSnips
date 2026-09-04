import unittest
from typing import List
from parameterized import parameterized
from utils.test_utils import custom_test_name_func
from algorithms.dynamic_programming.max_subarray import (
    find_max_sub_array,
    max_sub_array,
    max_subarray_sum_circular,
    max_subarray_sum_circular_2,
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

MAX_SUB_ARRAY_SUM_CIRCULAR_TEST_CASES = [
    ([1, -2, 3, -2], 3),
    ([5, -3, 5], 10),
    ([-3, -2, -3], -2),
    ([-7], -7),
    ([-7], -7),
    ([-4, -2, -9, -3], -2),
    ([5, 0, 2, 1], 8),
    ([-2, 6, -1, 4, -5, 2], 9),
    ([9, -8, 10, -1, 3], 21),
]


class MaxSubArrayTestCases(unittest.TestCase):
    @parameterized.expand(MAX_SUB_ARRAY_TEST_CASES, name_func=custom_test_name_func)
    def test_find_max_sub_array(self, nums: List[int], expected: int):
        actual = find_max_sub_array(nums)
        self.assertEqual(expected, actual)

    @parameterized.expand(MAX_SUB_ARRAY_TEST_CASES, name_func=custom_test_name_func)
    def test_max_sub_array(self, nums: List[int], expected: int):
        actual = max_sub_array(nums)
        self.assertEqual(expected, actual)

    @parameterized.expand(
        MAX_SUB_ARRAY_SUM_CIRCULAR_TEST_CASES, name_func=custom_test_name_func
    )
    def test_max_sub_array_sum_circular(self, nums: List[int], expected: int):
        actual = max_subarray_sum_circular(nums)
        self.assertEqual(expected, actual)

    @parameterized.expand(
        MAX_SUB_ARRAY_SUM_CIRCULAR_TEST_CASES, name_func=custom_test_name_func
    )
    def test_max_sub_array_sum_circular_2(self, nums: List[int], expected: int):
        actual = max_subarray_sum_circular_2(nums)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
