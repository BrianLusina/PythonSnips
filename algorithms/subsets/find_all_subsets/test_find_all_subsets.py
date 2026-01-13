import unittest
from typing import List
from parameterized import parameterized
from algorithms.subsets.find_all_subsets import find_all_subsets

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
]


class FindAllSubsetsTestCase(unittest.TestCase):
    @parameterized.expand(FIND_ALL_SUBSETS_TEST_CASES)
    def test_find_all_subsets(self, nums: List[int], expected: List[List[int]]):
        actual = find_all_subsets(nums)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
