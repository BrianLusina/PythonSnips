import unittest
from typing import List
from parameterized import parameterized
from algorithms.two_pointers.sort_by_parity import sort_array_by_parity_2

SORT_BY_PARITY_II_TEST_CASES = [
    ([3, 6, 1, 4], [6, 3, 4, 1]),
    ([2, 21, 12, 1], [2, 21, 12, 1]),
    ([0, 0, 1, 1], [0, 1, 0, 1]),
    ([100, 200, 300, 400], [100, 200, 300, 400]),
    ([10, 100, 1000, 10000], [10, 100, 1000, 10000]),
    ([4, 2, 5, 7], [4, 5, 2, 7]),
    ([2, 3], [2, 3]),
    ([3, 0, 4, 0, 2, 1, 3, 1, 3, 4], [0, 3, 4, 3, 2, 1, 0, 1, 4, 3]),
]


class SortArrayByParityIITestCase(unittest.TestCase):
    @parameterized.expand(SORT_BY_PARITY_II_TEST_CASES)
    def test_sort_array_by_parity(self, nums: List[int], expected: List[int]):
        actual = sort_array_by_parity_2(nums)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
