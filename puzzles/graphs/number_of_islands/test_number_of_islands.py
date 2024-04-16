import unittest
from . import num_of_islands


class NumberOfIslandsTestCase(unittest.TestCase):
    def test_number_of_islands_with_1_large_island(self):
        grid = [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
        ]
        expected = 1
        actual = num_of_islands(grid)
        self.assertEqual(expected, actual)

    def test_number_of_islands_with_3_islands(self):
        grid = [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"],
        ]
        expected = 3
        actual = num_of_islands(grid)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
