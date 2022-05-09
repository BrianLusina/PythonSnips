import unittest

from puzzles.maxareaofisland import max_area_of_island


class TestMaxAreaOfIsland(unittest.TestCase):

    def test_empty_grid(self):
        """should return 0 for empty grid"""
        grid = [[]]
        expected = 0
        self.assertEqual(max_area_of_island(grid), expected)

    def test_grid_with_no_islands(self):
        """should return 0 for grid with no islands"""
        grid = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        expected = 0
        actual = max_area_of_island(grid)
        self.assertEqual(expected, actual)

    def test_should_return_max_area_of_island(self):
        grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
        expected = 6
        actual = max_area_of_island(grid)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
