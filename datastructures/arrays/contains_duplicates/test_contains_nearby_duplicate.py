import unittest
from typing import List
from parameterized import parameterized
from datastructures.arrays.contains_duplicates import (
    contains_nearby_duplicate,
    contains_nearby_duplicates_2,
)


class ContainsNearbyDuplicateTestCases(unittest.TestCase):
    @parameterized.expand(
        [
            ([7, 8, 6, 7, 9], 3, True),
            ([7, 8, 6, 7, 6, 9], 2, True),
            ([900], 900, False),
            ([9, -6, 3, 0, -3, -6, 9], 5, True),
            ([1, 2, 3, 1, 2, 3], 2, False),
            ([1, 0, 1, 1], 1, True),
            ([1, 2, 3, 1], 3, True),
        ]
    )
    def test_contains_duplicates(self, nums: List[int], k: int, expected: bool):
        actual = contains_nearby_duplicate(nums, k)
        self.assertEqual(expected, actual)

    @parameterized.expand(
        [
            ([7, 8, 6, 7, 9], 3, True),
            ([7, 8, 6, 7, 6, 9], 2, True),
            ([900], 900, False),
            ([1, 2, 3, 1, 2, 3], 2, False),
            ([1, 0, 1, 1], 1, True),
            ([1, 2, 3, 1], 3, True),
        ]
    )
    def test_contains_duplicates_2(self, nums: List[int], k: int, expected: bool):
        actual = contains_nearby_duplicates_2(nums, k)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
