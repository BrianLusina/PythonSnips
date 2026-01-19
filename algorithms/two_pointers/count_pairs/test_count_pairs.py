import unittest
from typing import List
from parameterized import parameterized
from algorithms.two_pointers.count_pairs import count_pairs


COUNT_PAIRS_TEST_CASES = [
    ([1, 3, 2, 4, 5], 6, 4),
    ([10, 20, 30, 40], 50, 2),
    ([5, 1, 3, 2], 7, 4),
    ([-1, 9, 17, 11, 6], 3, 0),
    ([20, 20, 20, 20, 20, 20], 7, 0),
    ([-5, -4, -3], -5, 3),
    ([-1, 1, 2, 3, 1], 2, 3),
    ([-6, 2, 5, -2, -7, -1, 3], -2, 10),
]


class CountPairsTestCase(unittest.TestCase):
    @parameterized.expand(COUNT_PAIRS_TEST_CASES)
    def test_count_pairs(self, nums: List[int], target: int, expected: int):
        actual = count_pairs(nums, target)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
