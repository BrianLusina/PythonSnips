import unittest
from typing import List
from parameterized import parameterized
from algorithms.prefix_sum.continous_sub_array_sum import check_subarray_sum

CHECK_SUBARRAY_SUM_TEST_CASES = [
    ([23, 2, 4, 6, 7], 6, True),
    ([1, 2, 3], 5, True),
    ([5, 0, 0, 3], 3, True),
    ([0, 3], 2, False),
    ([5, 3, 4, 2], 19, False),
    ([5, 3, 4, 2, 7, 3], 8, True),
]


class ContinuousSubarraySumTestCase(unittest.TestCase):
    @parameterized.expand(CHECK_SUBARRAY_SUM_TEST_CASES)
    def test_check_subarray_sum(self, nums: List[int], k: int, expected: bool):
        actual = check_subarray_sum(nums, k)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
