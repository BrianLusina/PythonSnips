import unittest
from typing import List
from parameterized import parameterized
from algorithms.greedy.create_maximum_number import max_number

CREATE_MAXIMUM_NUMBER_TEST_CASES = [
    ([2, 5, 1], [4, 3], 4, [5, 4, 3, 1]),
    ([7, 1, 6], [5, 9], 3, [9, 7, 6]),
    ([8, 0, 8], [9], 3, [9, 8, 8]),
    ([1, 4, 2], [6, 5, 3], 5, [6, 5, 4, 3, 2]),
    ([3, 3, 9], [3, 4, 3], 4, [9, 3, 4, 3]),
    ([3, 4, 6, 5], [9, 1, 2, 5, 8, 3], 5, [9, 8, 6, 5, 3]),
    ([6, 7], [6, 0, 4], 5, [6, 7, 6, 0, 4]),
    ([3, 9], [8, 9], 3, [9, 8, 9]),
]


class CreateMaximumNumberTestCase(unittest.TestCase):
    @parameterized.expand(CREATE_MAXIMUM_NUMBER_TEST_CASES)
    def test_create_maximum_number(
        self, nums1: List[int], nums2: List[int], k: int, expected: List[int]
    ):
        actual = max_number(nums1, nums2, k)
        self.assertListEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
