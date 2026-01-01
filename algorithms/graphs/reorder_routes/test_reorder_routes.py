import unittest
from typing import List
from parameterized import parameterized
from algorithms.graphs.reorder_routes import min_reorder

REORDER_ROUTES_TEST_CASES = [
    (6, [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]], 3),
    (5, [[1, 0], [1, 2], [3, 2], [3, 4]], 2),
    (3, [[1, 0], [2, 0]], 0),
    (4, [[0, 1], [1, 2], [2, 3]], 3),
    (6, [[0, 1], [2, 0], [3, 2], [4, 3], [5, 4]], 1),
    (5, [[1, 0], [2, 1], [3, 2], [4, 3]], 0),
    (7, [[0, 1], [2, 0], [3, 2], [4, 3], [5, 3], [6, 5]], 1),
]


class ReorderRoutesTestCase(unittest.TestCase):
    @parameterized.expand(REORDER_ROUTES_TEST_CASES)
    def test_min_reorder_routes(
        self, n: int, connections: List[List[int]], expected: int
    ):
        actual = min_reorder(n, connections)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
