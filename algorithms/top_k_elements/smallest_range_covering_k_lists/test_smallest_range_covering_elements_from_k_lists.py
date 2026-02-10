import unittest
from typing import List
from parameterized import parameterized
from algorithms.top_k_elements.smallest_range_covering_k_lists import smallest_range

SMALLEST_RANGE_COVERING_ELEMENTS_FROM_K_LISTS_TESTS = [
    ([[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]], [20, 24]),
    ([[1, 2, 3], [1, 2, 3], [1, 2, 3]], [1, 1]),
    ([[1, 5, 8], [4, 12], [7, 8, 10]], [4, 7]),
    ([[2, 6, 10], [1, 5, 9], [4, 8, 12]], [4, 6]),
    ([[1, 3, 7], [2, 4, 8], [5, 6, 9]], [3, 5]),
    ([[1, 5], [3, 7], [4, 6]], [3, 5]),
    ([[1, 5], [4, 6], [6, 8], [11, 15]], [5, 11]),
    ([[1, 5]], [1, 1]),
    ([[1, 9], [3, 8], [4, 4]], [1, 4]),
    ([[1, 2], [3, 4], [8, 8]], [2, 8]),
]


class SmallestRangeCoveringElementsFromKListsTestCase(unittest.TestCase):
    @parameterized.expand(SMALLEST_RANGE_COVERING_ELEMENTS_FROM_K_LISTS_TESTS)
    def test_smallest_range(self, nums: List[List[int]], expected: List[int]):
        actual = smallest_range(nums)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
