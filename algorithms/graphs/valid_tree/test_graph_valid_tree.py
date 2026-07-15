import unittest
from typing import List
from parameterized import parameterized
from algorithms.graphs.valid_tree import valid_tree

GRAPH_VALID_TREE_TEST_CASES = [
    ("n=5, edges=[[0,1],[0,2],[0,3],[3,4]]", 5, [[0, 1], [0, 2], [0, 3], [3, 4]], True),
    (
        "n=5, edges=[[0,1],[0,2],[0,3],[0,4],[3,4]]",
        5,
        [[0, 1], [0, 2], [0, 3], [0, 4], [3, 4]],
        False,
    ),
    (
        "n=6, edges=[[0,1],[0,2],[1,3],[2,4],[0,5]]",
        6,
        [[0, 1], [0, 2], [1, 3], [2, 4], [0, 5]],
        True,
    ),
    ("n=4, edges=[[0,1],[0,2],[0,3]]", 4, [[0, 1], [0, 2], [0, 3]], True),
    ("n=3, edges=[[0,1],[0,2],[1,2]]", 3, [[0, 1], [0, 2], [1, 2]], False),
]


class GraphValidTreeTestCase(unittest.TestCase):
    @parameterized.expand(GRAPH_VALID_TREE_TEST_CASES)
    def test_graph_valid_tree(self, _, n: int, edges: List[List[int]], expected: bool):
        actual = valid_tree(n, edges)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
