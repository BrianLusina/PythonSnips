import unittest
from parameterized import parameterized
from utils.test_utils import custom_test_name_func
from bit_manipulation.bitwise_ors_of_subarrays import (
    subarray_bitwise_ors,
    subarray_bitwise_ors_2,
)

BITWISE_ORS_TEST_CASES = [
    ([0], 1),
    ([1, 1, 2], 3),
    ([1, 2, 4], 6),
    ([37], 1),
    ([0, 0, 0, 0, 0], 1),
    ([6, 6, 6, 6], 1),
    ([1, 2, 4, 8], 10),
    ([0, 3, 0, 5], 4),
]


class SubarrayBitwiseOrsTestCase(unittest.TestCase):
    @parameterized.expand(BITWISE_ORS_TEST_CASES, name_func=custom_test_name_func)
    def test_bitwise_ors_of_subarrays(self, nums: list[int], expected: int):
        actual = subarray_bitwise_ors(nums)
        self.assertEqual(expected, actual)

    @parameterized.expand(BITWISE_ORS_TEST_CASES, name_func=custom_test_name_func)
    def test_subarray_bitwise_ors_2(self, nums: list[int], expected: int):
        actual = subarray_bitwise_ors_2(nums)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
