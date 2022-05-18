import unittest

from puzzles.number_of_provinces import number_of_provinces


class NumberOfProvincesTestCase(unittest.TestCase):
    def test_empty_grid(self):
        """returns 0 for an empty grid"""
        is_connected = []
        actual = number_of_provinces(is_connected)
        expected = 0
        self.assertEqual(actual, expected)

    def test_returns_2_for_3_cities_in_grid(self):
        """returns 2 for a grid of  [[1,1,0],[1,1,0],[0,0,1]]"""
        is_connected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
        actual = number_of_provinces(is_connected)
        expected = 2
        self.assertEqual(actual, expected)

    def test_returns_3_for_3_cities_in_grid(self):
        """returns 3 for a grid of [[1,0,0],[0,1,0],[0,0,1]]"""
        is_connected = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
        actual = number_of_provinces(is_connected)
        expected = 3
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
