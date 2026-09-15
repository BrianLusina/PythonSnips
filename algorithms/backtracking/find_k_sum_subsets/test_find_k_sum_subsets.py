import unittest
from typing import List
from parameterized import parameterized
from utils.test_utils import custom_test_name_func
from algorithms.backtracking.find_k_sum_subsets import (
    get_k_sum_subsets,
    get_k_sum_subsets_backtrack,
    get_k_sum_subsets_with_bit,
)

FIND_K_SUM_SUBSETS_TEST_CASES = [
    ([8, 13, 3, 22, 17, 39, 87, 45, 36], 3, [[3]]),
    ([8, 13, 3, 22, 17, 39, 87, 45, 36], 47, [[8, 3, 36], [8, 22, 17], [8, 39]]),
    ([8, 13, 3, 22, 17, 39, 87, 45, 36], 135, [[8, 13, 22, 17, 39, 36], [3, 87, 45]]),
    (
        [8, 13, 3, 22, 17, 39, 87, 45, 36],
        100,
        [
            [8, 17, 39, 36],
            [13, 3, 22, 17, 45],
            [13, 3, 39, 45],
            [13, 87],
            [3, 22, 39, 36],
        ],
    ),
    ([8, 13, 3, 22, 17, 39, 87, 45, 36], 270, [[8, 13, 3, 22, 17, 39, 87, 45, 36]]),
]


class FindKSumSubsetsTestCase(unittest.TestCase):
    @parameterized.expand(
        FIND_K_SUM_SUBSETS_TEST_CASES, name_func=custom_test_name_func
    )
    def test_find_k_sum_subsets(
        self, nums: List[int], k: int, expected: List[List[int]]
    ):
        actual = get_k_sum_subsets(nums, k)
        self.assertEqual(expected, actual)

    @parameterized.expand(
        FIND_K_SUM_SUBSETS_TEST_CASES, name_func=custom_test_name_func
    )
    def test_find_k_sum_subsets_backtrack(
        self, nums: List[int], k: int, expected: List[List[int]]
    ):
        actual = get_k_sum_subsets_backtrack(nums, k)
        self.assertEqual(expected, actual)

    @parameterized.expand(
        FIND_K_SUM_SUBSETS_TEST_CASES, name_func=custom_test_name_func
    )
    def test_find_k_sum_subsets_with_bit(
        self, nums: List[int], k: int, expected: List[List[int]]
    ):
        actual = get_k_sum_subsets_with_bit(nums, k)
        self.assertEqual(sorted(expected), sorted(actual))


if __name__ == "__main__":
    unittest.main()
