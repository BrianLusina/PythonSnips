import unittest

from algorithms.flood_fill import flood_fill


class FloodFillTestCases(unittest.TestCase):
    def test_flood_fill_one(self):
        """[[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2"""
        image_grid = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
        sr = 1
        sc = 1
        color = 2
        expected = [[2, 2, 2], [2, 2, 0], [2, 0, 1]]
        actual = flood_fill(image=image_grid, sr=sr, sc=sc, new_color=color)
        self.assertEqual(expected, actual)

    def test_flood_fill_two(self):
        """[[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0"""
        image_grid = [[0, 0, 0], [0, 0, 0]]
        sr = 0
        sc = 0
        color = 0
        expected = [[0, 0, 0], [0, 0, 0]]
        actual = flood_fill(image=image_grid, sr=sr, sc=sc, new_color=color)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
