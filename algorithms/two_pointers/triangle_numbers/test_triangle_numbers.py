import unittest
from typing import List
from parameterized import parameterized
from algorithms.two_pointers.triangle_numbers import triangle_number

TRIANGLE_NUMBER_TEST_CASES = [
    ([11, 4, 9, 6, 15, 18], 10),
    ([2, 2, 3, 4], 3),
    ([4, 2, 3, 4], 4),
]


class TriangleNumberTestCases(unittest.TestCase):
    @parameterized.expand(TRIANGLE_NUMBER_TEST_CASES)
    def test_triangle_number(self, heights: List[int], expected: int):
        actual = triangle_number(heights)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
