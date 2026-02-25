import unittest
from typing import List
from parameterized import parameterized
from algorithms.search.binary_search.min_in_rotated_sorted_array import (
    find_min,
    find_min_with_duplicates,
    find_min_with_duplicates_2,
)

MIN_IN_ROTATED_SORTED_ARRAY_TEST_CASES = [
    ([3, 4, 5, 1, 2], 1),
    ([4, 5, 6, 7, 0, 1, 2], 0),
    ([11, 13, 15, 17], 11),
    ([30, 40, 50, 10, 20], 10),
    ([3, 5, 7, 11, 13, 17, 19, 2], 2),
    ([4, 5, 6, 7, 0, 1, 4], 0),
    ([8], 8),
    ([500, 600, 700, 800, 900, 1000], 500),
    ([-5, -3, -2, 0, 2, 3, 5, 7, 11, -11, -7], -11),
    ([64, 128, 256, 256, 512, 2, 4, 8, 16, 16, 16, 32, 64], 2),
    ([1, 3, 5], 1),
    ([2, 2, 2, 0, 1], 0),
]

MIN_IN_ROTATED_SORTED_ARRAY_II_TEST_CASES = [
    ([3, 3, 1, 3], 1),
]

MIN_IN_ROTATED_SORTED_ARRAY_II_TEST_CASES.extend(MIN_IN_ROTATED_SORTED_ARRAY_TEST_CASES)


class TestFinMinInRotatedSortedArray(unittest.TestCase):
    @parameterized.expand(MIN_IN_ROTATED_SORTED_ARRAY_TEST_CASES)
    def test_find_min(self, nums: List[int], expected: int):
        actual = find_min(nums)
        self.assertEqual(expected, actual)

    @parameterized.expand(MIN_IN_ROTATED_SORTED_ARRAY_II_TEST_CASES)
    def test_find_min_with_duplicates(self, nums: List[int], expected: int):
        actual = find_min_with_duplicates(nums)
        self.assertEqual(expected, actual)

    @parameterized.expand(MIN_IN_ROTATED_SORTED_ARRAY_II_TEST_CASES)
    def test_find_min_with_duplicates_2(self, nums: List[int], expected: int):
        actual = find_min_with_duplicates_2(nums)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
