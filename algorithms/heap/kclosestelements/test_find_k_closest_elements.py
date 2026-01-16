import unittest
from typing import List
from parameterized import parameterized
from algorithms.heap.kclosestelements import k_closest

K_CLOSEST_ELEMENTS_TEST_CASES = [
    ([1, 2, 3, 4, 5], 4, 3, [1, 2, 3, 4]),
    ([1, 3, 5, 8, 10], 2, 5, [3, 5]),
    ([3, 4, 7, 10, 15], 3, 8, [4, 7, 10]),
    ([5, 6, 7, 8, 9], 3, 7, [6, 7, 8]),
    ([1, 1, 1, 10, 10, 10], 1, 9, [10]),
    ([1, 2, 3, 4, 5], 2, 6, [4, 5]),
]


class KClosestElementsTestCase(unittest.TestCase):
    @parameterized.expand(K_CLOSEST_ELEMENTS_TEST_CASES)
    def test_k_closest_elements(
        self, nums: List[int], k: int, target: int, expected: List[int]
    ):
        actual = k_closest(nums, k, target)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
