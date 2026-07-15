import unittest
from typing import List
from parameterized import parameterized
from algorithms.two_pointers.max_score import max_sum

MAX_SCORE_TEST_CASES = [
    ([2, 4, 5, 8, 10], [4, 6, 8, 9], 30),
    ([1, 3, 5, 7, 9], [3, 5, 100], 109),
    ([1, 2, 3, 4, 5], [6, 7, 8, 9, 10], 40),
    ([2, 5, 7, 11, 13], [1, 4, 6, 8, 10], 38),
    ([1, 2, 4, 6, 8], [2, 4, 6, 7, 9], 29),
    ([1, 2, 5, 7], [3, 5, 6, 7, 8], 29),
    ([1, 4, 6, 7, 8], [2, 4, 5, 9, 10], 30),
    ([4, 6, 7, 10], [1, 2, 4, 5, 10], 30),
]


class MaxScoreTestCase(unittest.TestCase):
    @parameterized.expand(MAX_SCORE_TEST_CASES)
    def test_max_sum(self, nums1: List[int], nums2: List[int], expected: int):
        actual = max_sum(nums1, nums2)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
