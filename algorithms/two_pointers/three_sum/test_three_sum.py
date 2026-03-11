import unittest
from typing import List
from parameterized import parameterized
from algorithms.two_pointers.three_sum import three_sum, three_number_sum

THREE_SUM_TEST_CASES = [
    ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
    ([0, 1, 1], []),
    ([0, 0, 0], [[0, 0, 0]]),
    ([-1, 0, 1, 2, -1, -1], [[-1, -1, 2], [-1, 0, 1]]),
    ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
    ([-1, 0, 1, 2, -1, -4, 2], [[-1, -1, 2], [-1, 0, 1], [-4, 2, 2]]),
    ([-1, -1, 0, 1, 1, 1, 2], [[-1, -1, 2], [-1, 0, 1]]),
    ([-1, 0, 1, 2, -1, -4, -1, 2, 1], [[-1, -1, 2], [-1, 0, 1], [-4, 2, 2]]),
]

THREE_NUMBER_SUM_TEST_CASES = [
    ([12, 3, 1, 2, -6, 5, -8, 6], 0, [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]),
]


class ThreeSumTestCases(unittest.TestCase):
    @parameterized.expand(THREE_SUM_TEST_CASES)
    def test_three_sum(self, nums: List[int], expected: List[List[int]]):
        actual = three_sum(nums)
        self.assertEqual(expected, actual)


class ThreeNumberSumTestCases(unittest.TestCase):
    @parameterized.expand(THREE_NUMBER_SUM_TEST_CASES)
    def test_three_number_sum(
        self, nums: List[int], target_sum: int, expected: List[List[int]]
    ):
        actual = three_number_sum(nums, target_sum)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
