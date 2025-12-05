import unittest
from typing import List
from parameterized import parameterized
from datastructures.graphs.undirected.utils import closest_node


class ClosestNodeToPathInTreeTestCase(unittest.TestCase):

    @parameterized.expand(
        [
            (3, [[0, 1], [1, 2]], [[0, 2, 1]], [1]),
            (4, [[0, 1], [1, 2], [1, 3]], [[2, 3, 0]], [1]),
            (
                6,
                [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5]],
                [[1, 5, 2], [2, 3, 4]],
                [0, 0],
            ),
            (
                7,
                [[0, 1], [0, 2], [0, 3], [1, 4], [2, 5], [2, 6]],
                [[5, 3, 4], [5, 3, 6]],
                [0, 2],
            ),
            (3, [[0, 1], [1, 2]], [[0, 1, 2]], [1]),
            (3, [[0, 1], [1, 2]], [[0, 0, 0]], [0]),
        ]
    )
    def test_closest_node(
        self, n: int, edges: List[List[int]], query: List[List[int]], expected: int
    ):
        actual = closest_node(n, edges, query)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
