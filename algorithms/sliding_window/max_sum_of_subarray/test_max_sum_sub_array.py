import unittest
from typing import List
from parameterized import parameterized
from algorithms.sliding_window.max_sum_of_subarray import (
    max_sum_subarray,
    max_sum_subarray_2,
    max_sum_subarray_3,
)

MAX_SUM_SUBARRAY_OF_SIZE_K = [
    ([2, 1, 5, 1, 3, 2], 3, 9),
    ([4, 2, -1, 9, 7, -3, 5], 4, 18),
    ([4, 2, 4, 5, 6], 4, 17),
    ([1, 2, 3, 4, 5], 2, 9),
    ([1, 1, 1, 1, 1], 1, 1),
    ([5, 5, 5, 5, 5], 3, 15),
    ([1, 2, 3, 1, 2, 3], 3, 6),
    ([1, 2, 1, 3, 1, 1, 1], 3, 6),
    ([1, 2, 3, 4, 5, 6], 5, 20),
]


class MaxSumSubArrayOfSizeKTestCase(unittest.TestCase):
    @parameterized.expand(MAX_SUM_SUBARRAY_OF_SIZE_K)
    def test_max_sum_subarray_size_k(self, nums: List[int], k: int, expected: int):
        actual = max_sum_subarray(nums, k)
        self.assertEqual(expected, actual)

    @parameterized.expand(MAX_SUM_SUBARRAY_OF_SIZE_K)
    def test_max_sum_subarray_size_k_2(self, nums: List[int], k: int, expected: int):
        actual = max_sum_subarray_2(nums, k)
        self.assertEqual(expected, actual)

    @parameterized.expand(MAX_SUM_SUBARRAY_OF_SIZE_K)
    def test_max_sum_subarray_size_k_3(self, nums: List[int], k: int, expected: int):
        actual = max_sum_subarray_3(nums, k)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
