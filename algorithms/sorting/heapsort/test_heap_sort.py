import unittest
from typing import List
from parameterized import parameterized
from algorithms.sorting.heapsort import heapsort, heapsort_2

TEST_CASES = [
    ([5, 2, 3, 1], [1, 2, 3, 5]),
    ([9, -3, 5, 0, -10, 8], [-10, -3, 0, 5, 8, 9]),
    ([2, 2, 1, 3, 1], [1, 1, 2, 2, 3]),
    ([4, -1, -1, 2, -2, 0], [-2, -1, -1, 0, 2, 4]),
    ([0, 0, 0, 0], [0, 0, 0, 0]),
]


class HeapSortTestCase(unittest.TestCase):
    @parameterized.expand(TEST_CASES)
    def test_heap_sort(self, nums: List[int], expected: List[int]):
        heapsort(nums)
        self.assertEqual(expected, nums)

    @parameterized.expand(TEST_CASES)
    def test_heap_sort_2(self, nums: List[int], expected: List[int]):
        actual = heapsort_2(nums)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
