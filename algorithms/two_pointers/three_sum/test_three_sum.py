import unittest
from typing import List
from parameterized import parameterized
from algorithms.two_pointers.three_sum import three_sum

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


class ThreeSumTestCases(unittest.TestCase):
    @parameterized.expand(THREE_SUM_TEST_CASES)
    def test_three_sum(self, nums: List[int], expected: List[List[int]]):
        actual = three_sum(nums)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
