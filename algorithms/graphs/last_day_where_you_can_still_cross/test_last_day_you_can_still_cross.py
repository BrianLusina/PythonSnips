import unittest
from typing import List
from parameterized import parameterized
from algorithms.graphs.last_day_where_you_can_still_cross import (
    latest_day_to_cross_binary_search,
    last_day_to_cross_union_find,
)

LAST_DAY_TO_CROSS_TEST_CASES = [
    (2, 2, [[1, 1], [2, 1], [1, 2], [2, 2]], 2),
    (2, 2, [[1, 1], [1, 2], [2, 1], [2, 2]], 1),
    (3, 3, [[1, 2], [2, 1], [3, 3], [2, 2], [1, 1], [1, 3], [2, 3], [3, 2], [3, 1]], 3),
    (
        3,
        4,
        [
            [2, 4],
            [1, 3],
            [3, 3],
            [2, 1],
            [2, 3],
            [2, 2],
            [1, 4],
            [3, 1],
            [1, 1],
            [1, 2],
            [3, 2],
            [3, 4],
        ],
        5,
    ),
    (
        5,
        5,
        [
            [1, 1],
            [2, 1],
            [3, 1],
            [4, 1],
            [5, 1],
            [1, 2],
            [2, 2],
            [3, 2],
            [4, 2],
            [5, 2],
            [1, 3],
            [2, 3],
            [3, 3],
            [4, 3],
            [5, 3],
            [1, 4],
            [2, 4],
            [3, 4],
            [4, 4],
            [5, 4],
            [1, 5],
            [2, 5],
            [3, 5],
            [4, 5],
            [5, 5],
        ],
        20,
    ),
]


class LastDayToCrossTestCase(unittest.TestCase):
    @parameterized.expand(LAST_DAY_TO_CROSS_TEST_CASES)
    def test_latest_day_to_cross_binary_search(
        self, rows, cols, cells: List[List[int]], expected: int
    ):
        actual = latest_day_to_cross_binary_search(rows, cols, cells)
        self.assertEqual(expected, actual)

    @parameterized.expand(LAST_DAY_TO_CROSS_TEST_CASES)
    def test_last_day_to_cross_union_find(
        self, rows, cols, cells: List[List[int]], expected: int
    ):
        actual = last_day_to_cross_union_find(rows, cols, cells)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
