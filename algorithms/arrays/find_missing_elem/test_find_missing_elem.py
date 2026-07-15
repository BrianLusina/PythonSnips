import unittest
from typing import List
from parameterized import parameterized
from . import (
    find_missing_element,
    find_missing_number,
    find_missing_number_sum_of_n_terms,
)

FIND_MISSING_ELEMENT_TEST_CASES = [
    ([0, 2, 3, 4, 5], 1),
    ([0, 1, 2, 3, 5, 6, 7], 4),
    ([0, 1, 2, 3, 4, 5, 6, 7], 8),
    ([1], 0),
    ([1, 0, 2, 3, 4, 5, 6, 8, 9, 7, 11], 10),
    ([1, 4, 5, 6, 8, 2, 0, 7], 3),
    ([3, 0, 1, 4], 2),
    ([0, 1, 2, 4], 3),
    ([9, 6, 4, 2, 3, 5, 7, 0, 1], 8),
    ([0, 1], 2),
    ([3, 0, 1], 2),
    ([8, 2, 4, 5, 3, 7, 1, 0], 6),
    ([0, 1, 2, 3, 5], 4),
]


class FindMissingElementTestCases(unittest.TestCase):
    @parameterized.expand(FIND_MISSING_ELEMENT_TEST_CASES)
    def test_find_missing_element(self, nums: List[int], expected: int):
        actual = find_missing_element(nums)
        self.assertEqual(expected, actual)

    @parameterized.expand(FIND_MISSING_ELEMENT_TEST_CASES)
    def test_find_missing_number(self, nums: List[int], expected: int):
        actual = find_missing_number(nums)
        self.assertEqual(expected, actual)

    @parameterized.expand(FIND_MISSING_ELEMENT_TEST_CASES)
    def test_find_missing_number_sum_of_n_terms(self, nums: List[int], expected: int):
        actual = find_missing_number_sum_of_n_terms(nums)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
