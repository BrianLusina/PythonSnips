import unittest
from typing import List
from parameterized import parameterized
from utils.test_utils import custom_test_name_func
from algorithms.matrix.game_of_life import game_of_life


GAME_OF_LIFE_TEST_CASES = [
    ([[1]], [[0]]),
    ([[1, 1], [1, 1]], [[1, 1], [1, 1]]),
    ([[0, 1, 0], [0, 1, 0], [0, 1, 0]], [[0, 0, 0], [1, 1, 1], [0, 0, 0]]),
    ([[1, 0, 1], [0, 0, 0], [0, 1, 0]], [[0, 0, 0], [0, 1, 0], [0, 0, 0]]),
    ([[1, 1, 1], [1, 1, 0], [0, 0, 0]], [[1, 0, 1], [1, 0, 1], [0, 0, 0]]),
]


class GameOfLifeTestCase(unittest.TestCase):
    @parameterized.expand(GAME_OF_LIFE_TEST_CASES, name_func=custom_test_name_func)
    def test_game_of_life(self, board: List[List[int]], expected: List[List[int]]):
        board_copy = board[:]
        game_of_life(board_copy)
        self.assertEqual(expected, board_copy)


if __name__ == "__main__":
    unittest.main()
