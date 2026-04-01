import unittest
from typing import List
from parameterized import parameterized
from algorithms.graphs.shortest_path_length import shortest_path_length

SHORTEST_PATH_LENGTH_TEST_CASES = [
    ([[1, 2, 3], [0], [0], [0]], 4),
    ([[1], [0, 2, 4], [1, 3, 4], [2], [1, 2]], 4),
    ([[]], 0),
    ([[1], [0, 2], [1]], 2),
    ([[1, 3], [0, 2], [1, 3], [0, 2]], 3),
    ([[1, 5], [0, 2, 4], [1, 3], [2, 4], [1, 3, 5], [0, 4]], 5),
    ([[1, 2], [0, 2, 3], [0, 1, 3], [1, 2]], 3),
]


class ShortestPathLengthTestCase(unittest.TestCase):
    @parameterized.expand(SHORTEST_PATH_LENGTH_TEST_CASES)
    def test_shortest_path_length(self, graph: List[List[int]], expected: int):
        actual = shortest_path_length(graph)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
