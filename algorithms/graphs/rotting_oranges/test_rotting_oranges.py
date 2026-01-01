import unittest
from . import oranges_rotting


class RottingOrangesTestCase(unittest.TestCase):
    def test_1(self):
        """should return 4 for grid = [[2,1,1],[1,1,0],[0,1,1]]"""
        grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
        expected = 4
        actual = oranges_rotting(grid)
        self.assertEqual(expected, actual)

    def test_2(self):
        """should return -1 for grid = [[2,1,1],[0,1,1],[1,0,1]]"""
        grid = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
        expected = -1
        actual = oranges_rotting(grid)
        self.assertEqual(expected, actual)

    def test_3(self):
        """should return 0 for grid = [[0,2]]"""
        grid = [[0, 2]]
        expected = 0
        actual = oranges_rotting(grid)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
