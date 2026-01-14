import unittest
from typing import List
from parameterized import parameterized
from algorithms.heap.topkclosesttoorigin import (
    k_closest_to_origin,
    k_closest_to_origin_sorting,
)

TOP_K_CLOSEST_TO_ORIGIN = [
    ([[3, 4], [2, 2], [1, 1], [0, 0], [5, 5]], 3, [[2, 2], [1, 1], [0, 0]]),
    ([[1, 3], [-2, 2]], 1, [[-2, 2]]),
    ([[3, 3], [5, -1], [-2, 4]], 2, [[3, 3], [-2, 4]]),
]


class TopKClosestToOriginTestCase(unittest.TestCase):
    @parameterized.expand(TOP_K_CLOSEST_TO_ORIGIN)
    def test_top_k_closest_to_origin(
        self, points: List[List[int]], k: int, expected: List[List[int]]
    ):
        actual = k_closest_to_origin(points, k)

        sorted_expected = sorted(expected, key=lambda x: x[0])
        sorted_actual = sorted(actual, key=lambda x: x[0])
        self.assertEqual(sorted_expected, sorted_actual)

    @parameterized.expand(TOP_K_CLOSEST_TO_ORIGIN)
    def test_top_k_closest_to_origin_sorting(
        self, points: List[List[int]], k: int, expected: List[List[int]]
    ):
        actual = k_closest_to_origin_sorting(points, k)

        sorted_expected = sorted(expected, key=lambda x: x[0])
        sorted_actual = sorted(actual, key=lambda x: x[0])
        self.assertEqual(sorted_expected, sorted_actual)


if __name__ == "__main__":
    unittest.main()
