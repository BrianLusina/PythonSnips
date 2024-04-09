import unittest

from puzzles.doomsday_fuel import doomsday_fuel


class DoomsDayFuelTestCases(unittest.TestCase):
    def test_one(self):
        """Matrix of [[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
        should return [7, 6, 8, 21]"""
        matrix = [
            [0, 2, 1, 0, 0],
            [0, 0, 0, 3, 4],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ]
        expected = [7, 6, 8, 21]
        actual = doomsday_fuel(matrix)
        self.assertEqual(expected, actual)

    def test_two(self):
        """Matrix of [[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0]]
        should return [0, 3, 2, 9, 14]"""
        matrix = [
            [0, 1, 0, 0, 0, 1],
            [4, 0, 0, 3, 2, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
        ]
        expected = [0, 3, 2, 9, 14]
        actual = doomsday_fuel(matrix)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
