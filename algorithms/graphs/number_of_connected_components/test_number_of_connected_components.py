import unittest
from typing import List
from parameterized import parameterized
from utils.test_utils import custom_test_name_func
from algorithms.graphs.number_of_connected_components import (
    count_components_union_find,
    count_components_dfs,
    count_components_dfs_iterative
)

COUNT_COMPONENTS_TEST_CASES = [
    (5, [[0, 1], [1, 2], [3, 4]], 2),
    (6, [[0, 1], [3, 4], [4, 5]], 3),
    (2, [[0, 1]], 1),
    (8, [[0, 1], [1, 2], [4, 5], [6, 7]], 4),
    (10, [[0, 2], [2, 3], [4, 5], [5, 6], [7, 8], [8, 9]], 4),
]


class NumberOfConnectedComponentsInUndirectedGraphTestCase(unittest.TestCase):
    @parameterized.expand(COUNT_COMPONENTS_TEST_CASES, name_func=custom_test_name_func)
    def test_count_components_union_find(
        self, n: int, edges: List[List[int]], expected: int
    ):
        actual = count_components_union_find(n, edges)
        self.assertEqual(expected, actual)

    @parameterized.expand(COUNT_COMPONENTS_TEST_CASES, name_func=custom_test_name_func)
    def test_count_components_dfs(self, n: int, edges: List[List[int]], expected: int):
        actual = count_components_dfs(n, edges)
        self.assertEqual(expected, actual)

    @parameterized.expand(COUNT_COMPONENTS_TEST_CASES, name_func=custom_test_name_func)
    def test_count_components_dfs_iterative(self, n: int, edges: List[List[int]], expected: int):
        actual = count_components_dfs_iterative(n, edges)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
