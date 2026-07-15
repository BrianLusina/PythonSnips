import unittest
from typing import List, Union
from copy import deepcopy
from parameterized import parameterized
from algorithms.fast_and_slow.find_duplicate import (
    find_duplicate,
    find_duplicate_floyd_algo,
)

FIND_DUPLICATE_TEST_CASES = [
    ([3, 4, 1, 4, 2], 4),
    ([1, 2, 3], -1),
    ([3, 4, 1, 4, 1], [1, 4]),
    ([1, 3, 3, 4, 2, 5], 3),
    ([1, 5, 3, 4, 2, 5], 5),
    ([1, 2, 3, 4, 5, 6, 6, 7], 6),
    ([4, 6, 7, 7, 3, 5, 2, 8, 1], 7),
    ([9, 8, 7, 6, 2, 3, 5, 4, 1, 9], 9),
    ([3, 4, 4, 4, 2], 4),
    ([1, 1], 1),
    ([1, 3, 4, 2, 2], 2),
    ([1, 3, 6, 2, 7, 3, 5, 4], 3),
    ([1, 2, 2], 2),
]


class FindDuplicateTestCases(unittest.TestCase):
    @parameterized.expand(FIND_DUPLICATE_TEST_CASES)
    def test_find_duplicate_floyd_algo(
        self, nums: List[int], expected: Union[List[int], int]
    ):
        actual = find_duplicate_floyd_algo(nums)
        if type(expected) == list:
            self.assertIn(actual, expected)
        else:
            self.assertEqual(expected, actual)

    @parameterized.expand(FIND_DUPLICATE_TEST_CASES)
    def test_find_duplicate(self, nums: List[int], expected: Union[List[int], int]):
        numbers = deepcopy(nums)
        actual = find_duplicate(numbers)
        if type(expected) == list:
            self.assertIn(actual, expected)
        else:
            self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
