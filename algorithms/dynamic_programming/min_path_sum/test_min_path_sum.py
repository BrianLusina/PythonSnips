import unittest
from typing import List
from parameterized import parameterized
from algorithms.dynamic_programming.min_path_sum import min_path_sum, min_path_sum_2

TEST_CASES = [
    ([[5]], 5),
    ([[2], [3, 4]], 5),
    ([[1000], [2000, 3000]], 3000),
    ([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]], 11),
    ([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]], 17),
]


class MinPathSumInTriangleTestCase(unittest.TestCase):
    @parameterized.expand(TEST_CASES)
    def test_min_path_sum_in_triangle(self, triangle: List[List[int]], expected: int):
        actual = min_path_sum(triangle)
        self.assertEqual(expected, actual)

    @parameterized.expand(TEST_CASES)
    def test_min_path_sum_2_in_triangle(self, triangle: List[List[int]], expected: int):
        actual = min_path_sum_2(triangle)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
