import unittest
from . import nearest_exit


class NearestExitFromEntranceTestCase(unittest.TestCase):
    def test_1(self):
        """should return 1 for maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]], entrance = [1,2]"""
        maze = [["+", "+", ".", "+"], [".", ".", ".", "+"], ["+", "+", "+", "."]]
        entrance = [1, 2]
        expected = 1
        actual = nearest_exit(maze, entrance)
        self.assertEqual(expected, actual)

    def test_2(self):
        """should return 2 maze = [["+","+","+"],[".",".","."],["+","+","+"]], entrance = [1,0]"""
        maze = [["+", "+", "+"], [".", ".", "."], ["+", "+", "+"]]
        entrance = [1, 0]
        expected = 2
        actual = nearest_exit(maze, entrance)
        self.assertEqual(expected, actual)

    def test_3(self):
        """should return -1 for maze = [[".","+"]], entrance = [0,0]"""
        maze = [[".", "+"]]
        entrance = [0, 0]
        expected = -1
        actual = nearest_exit(maze, entrance)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
