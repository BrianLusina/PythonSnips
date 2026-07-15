import unittest
from typing import List
from parameterized import parameterized
from utils.test_utils import custom_test_name_func
from bit_manipulation.sum_of_subset_xor import subset_xor_sum


SUM_OF_ALL_SUBSET_XOR_TOTALS_TEST_CASES = [
    ([1], 1),
    ([20], 20),
    ([1, 2], 6),
    ([7], 7),
    ([15, 7, 3], 60),
    ([19, 5, 1, 3, 15, 13, 11], 1984),
    ([9, 12, 9, 3, 3, 20, 3, 1, 15], 7936),
    ([1, 3], 6),
    ([5, 1, 6], 28),
    ([3, 4, 5, 6, 7, 8], 480),
    ([5, 20], 42),
    ([1, 1, 1, 1], 8),
    ([3, 5, 7, 9, 11, 13, 15, 17, 19, 20], 15872),
]


class SumOfAllSubsetXorTotalsTestCase(unittest.TestCase):
    @parameterized.expand(
        SUM_OF_ALL_SUBSET_XOR_TOTALS_TEST_CASES, name_func=custom_test_name_func
    )
    def test_subset_xor_sum(self, nums: List[int], expected: int):
        actual = subset_xor_sum(nums)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
