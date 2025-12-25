import unittest
from typing import List
from parameterized import parameterized
from algorithms.intervals.full_bloom_flowers import (
    full_bloom_flowers,
    full_bloom_flowers_2,
)

TEST_CASES = [
    ([[5, 5]], [5], [1]),
    ([[3, 3], [3, 3], [3, 3]], [2, 3, 4], [0, 3, 0]),
    ([[2, 4], [6, 8]], [1, 5, 9], [0, 0, 0]),
    ([[1, 4], [2, 5], [3, 6]], [1, 2, 3, 4, 5, 6], [1, 2, 3, 3, 2, 1]),
    ([[1, 2], [100, 200], [300, 400]], [1, 150, 250, 350, 500], [1, 1, 0, 1, 0]),
]


class FullBloomFlowersTestCase(unittest.TestCase):
    @parameterized.expand(TEST_CASES)
    def test_full_bloom_flowers(
        self, flowers: List[List[int]], people: List[int], expected: List[int]
    ):
        actual = full_bloom_flowers(flowers, people)
        self.assertEqual(expected, actual)

    @parameterized.expand(TEST_CASES)
    def test_full_bloom_flowers(
        self, flowers: List[List[int]], people: List[int], expected: List[int]
    ):
        actual = full_bloom_flowers_2(flowers, people)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
