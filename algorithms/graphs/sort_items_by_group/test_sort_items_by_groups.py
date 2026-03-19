import unittest
from typing import List
from parameterized import parameterized
from algorithms.graphs.sort_items_by_group import sort_items

SORT_ITEMS_BY_GROUPS_TEST_CASES = [
    (
        8,
        2,
        [-1, -1, 1, 0, 0, 1, 0, -1],
        [[], [6], [5], [6], [3, 6], [], [], []],
        [6, 3, 4, 5, 2, 0, 7, 1],
    ),
    (8, 2, [-1, -1, 1, 0, 0, 1, 0, -1], [[], [6], [5], [6], [3], [], [4], []], []),
    (6, 2, [0, 0, 1, 1, -1, -1], [[], [0], [], [2], [1, 3], [4]], [0, 1, 2, 3, 4, 5]),
    (4, 1, [0, 0, 0, 0], [[], [0], [1], [2]], [0, 1, 2, 3]),
    (3, 1, [0, 0, 0], [[2], [0], [1]], []),
    (5, 3, [0, 0, 1, 1, -1], [[], [0], [3], [], [2]], [0, 1, 3, 2, 4]),
]


class SortItemsByGroupsTestCase(unittest.TestCase):
    @parameterized.expand(SORT_ITEMS_BY_GROUPS_TEST_CASES)
    def test_sort_items(
        self,
        n: int,
        m: int,
        group: List[int],
        before_items: List[List[int]],
        expected: List[int],
    ):
        actual = sort_items(n, m, group, before_items)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
