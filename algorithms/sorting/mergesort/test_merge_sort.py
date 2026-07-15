import unittest
from typing import List
from parameterized import parameterized
from algorithms.sorting.mergesort import merge_sort_in_place, merge_sort_out_of_place

TEST_CASES = [
    ([5, 2, 3, 1], [1, 2, 3, 5]),
    ([9, -3, 5, 0, -10, 8], [-10, -3, 0, 5, 8, 9]),
    ([2, 2, 1, 3, 1], [1, 1, 2, 2, 3]),
    ([4, -1, -1, 2, -2, 0], [-2, -1, -1, 0, 2, 4]),
    ([0, 0, 0, 0], [0, 0, 0, 0]),
]


class MergeSortTestCase(unittest.TestCase):
    @parameterized.expand(TEST_CASES)
    def test_merge_sort_in_place(self, nums: List[int], expected: List[int]):
        actual = merge_sort_in_place(nums)
        self.assertEqual(expected, actual)

    @parameterized.expand(TEST_CASES)
    def test_merge_sort_out_of_place(self, nums: List[int], expected: List[int]):
        actual = merge_sort_out_of_place(nums)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
