import unittest
from typing import List
from parameterized import parameterized
from algorithms.graphs.cat_and_mouse import cat_mouse_game

CAT_AND_MOUSE_GAME_TESTS = [
    ([[2, 5], [3], [0, 4, 5], [1, 4, 5], [2, 3], [0, 2, 3]], 0),
    ([[1, 3], [0], [3], [0, 2]], 1),
]


class CatAndMouseGameTestCase(unittest.TestCase):
    @parameterized.expand(CAT_AND_MOUSE_GAME_TESTS)
    def test_cat_and_mouse_game(self, graph: List[List[int]], expected: int):
        actual = cat_mouse_game(graph)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
