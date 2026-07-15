import unittest
from typing import List
from parameterized import parameterized
from algorithms.backtracking.subsets.find_all_subsets import (
    find_all_subsets,
    find_all_subsets_with_duplicates,
)

FIND_ALL_SUBSETS_TEST_CASES = [
    ([], []),
    ([9], [[], [9]]),
    ([1], [[], [1]]),
    ([0], [[], [0]]),
    ([2, 4], [[], [2], [4], [2, 4]]),
    ([1, 2], [[], [1], [2], [1, 2]]),
    ([2, 5, 7], [[], [2], [5], [2, 5], [7], [2, 7], [5, 7], [2, 5, 7]]),
    (
        [1, 2, 3, 4],
        [
            [],
            [1],
            [2],
            [1, 2],
            [3],
            [1, 3],
            [2, 3],
            [1, 2, 3],
            [4],
            [1, 4],
            [2, 4],
            [1, 2, 4],
            [3, 4],
            [1, 3, 4],
            [2, 3, 4],
            [1, 2, 3, 4],
        ],
    ),
    ([3, 6, 9], [[], [3], [3, 6], [3, 6, 9], [3, 9], [6], [6, 9], [9]]),
    ([1, 2, 3], [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]),
]

FIND_ALL_SUBSETS_WITH_DUPLICATES_TEST_CASES = [
    ([0], [[], [0]]),
    ([-1, 1], [[], [-1], [-1, 1], [1]]),
    ([1, 2, 2], [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]),
    ([0, 0], [[], [0], [0, 0]]),
    ([-2, -2, 1], [[], [-2], [-2, -2], [-2, -2, 1], [-2, 1], [1]]),
    ([1, 1], [[], [1], [1, 1]]),
    (
        [4, 4, 4, 1, 4],
        [
            [],
            [1],
            [1, 4],
            [1, 4, 4],
            [1, 4, 4, 4],
            [1, 4, 4, 4, 4],
            [4],
            [4, 4],
            [4, 4, 4],
            [4, 4, 4, 4],
        ],
    ),
]
FIND_ALL_SUBSETS_WITH_DUPLICATES_TEST_CASES.extend(FIND_ALL_SUBSETS_TEST_CASES)


class FindAllSubsetsTestCase(unittest.TestCase):
    @parameterized.expand(FIND_ALL_SUBSETS_TEST_CASES)
    def test_find_all_subsets(self, nums: List[int], expected: List[List[int]]):
        actual = find_all_subsets(nums)
        expected_sorted = sorted(expected)
        actual_sorted = sorted(actual)
        self.assertEqual(expected_sorted, actual_sorted)

    @parameterized.expand(FIND_ALL_SUBSETS_WITH_DUPLICATES_TEST_CASES)
    def test_find_all_subsets_with_duplicates(
        self, nums: List[int], expected: List[List[int]]
    ):
        actual = find_all_subsets_with_duplicates(nums)
        expected_sorted = sorted(expected)
        actual_sorted = sorted(actual)
        self.assertEqual(expected_sorted, actual_sorted)


if __name__ == "__main__":
    unittest.main()
