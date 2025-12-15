import unittest
from typing import List
from parameterized import parameterized
from puzzles.arrays.max_consecutive_ones import longest_ones, find_max_consecutive_ones


class MaxConsecutiveOnesTestCase(unittest.TestCase):

    @parameterized.expand([
        ([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2, 6),
        ([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3, 10),
    ])
    def test_longest_ones(self, nums: List[int], k: int, expected: int):
        actual = longest_ones(nums, k)
        self.assertEqual(expected, actual)

    @parameterized.expand([
        ([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 4),
        ([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 4),
        ([1,1,0,0,1,1,1,0,0,1,0], 3),
        ([1,1,0,0,1,1], 2),
        ([1,1,1,0,1,1,1,1], 4),
        ([0,0,0,0], 0),
    ])
    def test_find_max_consecutive_ones(self, nums: List[int], expected: int):
        actual = find_max_consecutive_ones(nums)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
