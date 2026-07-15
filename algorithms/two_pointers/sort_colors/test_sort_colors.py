import unittest
from typing import List
from parameterized import parameterized
from algorithms.two_pointers.sort_colors import sort_colors

SORT_COLORS_TEST_CASES = [
    ([1, 0, 2, 1, 2, 2], [0, 1, 1, 2, 2, 2]),
    ([0, 1, 1, 2, 0, 2, 0, 2, 1, 2], [0, 0, 0, 1, 1, 1, 2, 2, 2, 2]),
    ([0], [0]),
    ([0, 1, 0], [0, 0, 1]),
    ([1], [1]),
    ([2, 2], [2, 2]),
    ([1, 2, 0], [0, 1, 2]),
    ([2, 2, 1], [1, 2, 2]),
    ([2, 1, 2, 0, 1, 2, 2, 0], [0, 0, 1, 1, 2, 2, 2, 2]),
    ([1, 1, 0, 2], [0, 1, 1, 2]),
    ([2, 1, 1, 0, 0], [0, 0, 1, 1, 2]),
    ([2, 0, 2, 1, 1, 0], [0, 0, 1, 1, 2, 2]),
]


class SortColorsTestCase(unittest.TestCase):
    @parameterized.expand(SORT_COLORS_TEST_CASES)
    def test_sort_colors(self, colors: List[int], expected: List[int]):
        actual = sort_colors(colors)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
