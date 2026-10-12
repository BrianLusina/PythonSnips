import unittest
from parameterized import parameterized
from utils.test_utils import custom_test_name_func
from algorithms.heap.final_array_state_after_k_ops import (
    get_final_state,
    get_final_state_full_scan,
)

FINAL_ARRAY_STATE_AFTER_K_MULTIPLICATION_OPS_TEST_CASES = [
    ([2, 1, 3, 5, 6], 5, 2, [8, 4, 6, 5, 6]),
    ([1, 2], 3, 4, [16, 8]),
]


class FinalArrayStateAfterKOpsTestCase(unittest.TestCase):
    @parameterized.expand(
        FINAL_ARRAY_STATE_AFTER_K_MULTIPLICATION_OPS_TEST_CASES,
        name_func=custom_test_name_func,
    )
    def test_final_array_state_after_k_multiplication_ops(
        self, nums: list[int], k: int, multiplier: int, expected: list[int]
    ):
        nums_copy = nums.copy()
        actual = get_final_state(nums_copy, k, multiplier)
        self.assertEqual(expected, actual)

    @parameterized.expand(
        FINAL_ARRAY_STATE_AFTER_K_MULTIPLICATION_OPS_TEST_CASES,
        name_func=custom_test_name_func,
    )
    def test_final_array_state_after_k_multiplication_ops_full_scan(
        self, nums: list[int], k: int, multiplier: int, expected: list[int]
    ):
        nums_copy = nums.copy()
        actual = get_final_state_full_scan(nums_copy, k, multiplier)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
