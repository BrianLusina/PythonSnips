import unittest
from typing import List
from parameterized import parameterized
from algorithms.two_pointers.product_of_array_except_self import (
    product_except_self_prefix_sums,
    product_except_self_two_pointers,
)

PRODUCT_OF_ARRAY_EXCEPT_SELF_TEST_CASES = [
    ([1, 2, 3, 4], [24, 12, 8, 6]),
    ([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0]),
    ([1, -3, 5, 7, -11], [1155, -385, 231, 165, -105]),
    ([2, 4, 0, 6], [0, 0, 48, 0]),
    ([0, -1, 2, -3, 4, -2], [-48, 0, 0, 0, 0, 0]),
    ([5, 3, -1, 6, 4], [-72, -120, 360, -60, -90]),
    ([-7, 6, 4, 3, 1, 2], [144, -168, -252, -336, -1008, -504]),
]


class ProductOfArrayExceptSelfTestCases(unittest.TestCase):
    @parameterized.expand(PRODUCT_OF_ARRAY_EXCEPT_SELF_TEST_CASES)
    def test_product_of_array_except_self_prefix_sums(
        self, nums: List[int], expected: List[int]
    ):
        actual = product_except_self_prefix_sums(nums)
        self.assertEqual(expected, actual)

    @parameterized.expand(PRODUCT_OF_ARRAY_EXCEPT_SELF_TEST_CASES)
    def test_product_of_array_except_self_two_pointers(
        self, nums: List[int], expected: List[int]
    ):
        actual = product_except_self_two_pointers(nums)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
