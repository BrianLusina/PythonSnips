import unittest

from . import number_of_provinces, number_of_provinces_dfs


class NumberOfProvincesTestCase(unittest.TestCase):
    def test_empty_grid(self):
        """returns 0 for an empty grid"""
        is_connected = []
        actual = number_of_provinces(is_connected)
        expected = 0
        self.assertEqual(expected, actual)

    def test_returns_2_for_3_cities_in_grid(self):
        """returns 2 for a grid of  [[1,1,0],[1,1,0],[0,0,1]]"""
        is_connected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
        actual = number_of_provinces(is_connected)
        expected = 2
        self.assertEqual(expected, actual)

    def test_returns_3_for_3_cities_in_grid(self):
        """returns 3 for a grid of [[1,0,0],[0,1,0],[0,0,1]]"""
        is_connected = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
        actual = number_of_provinces(is_connected)
        expected = 3
        self.assertEqual(expected, actual)

    def test_returns_1_for_3_cities_in_grid(self):
        """returns 1 for a grid of [[1,1,1],[1,1,1],[1,1,1]]"""
        is_connected = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
        actual = number_of_provinces(is_connected)
        expected = 1
        self.assertEqual(expected, actual)


class NumberOfProvincesDfsTestCase(unittest.TestCase):
    def test_empty_grid(self):
        """returns 0 for an empty grid"""
        is_connected = []
        actual = number_of_provinces_dfs(is_connected)
        expected = 0
        self.assertEqual(expected, actual)

    def test_returns_2_for_3_cities_in_grid(self):
        """returns 2 for a grid of  [[1,1,0],[1,1,0],[0,0,1]]"""
        is_connected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
        actual = number_of_provinces_dfs(is_connected)
        expected = 2
        self.assertEqual(expected, actual)

    def test_returns_3_for_3_cities_in_grid(self):
        """returns 3 for a grid of [[1,0,0],[0,1,0],[0,0,1]]"""
        is_connected = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
        actual = number_of_provinces_dfs(is_connected)
        expected = 3
        self.assertEqual(expected, actual)

    def test_returns_1_for_3_cities_in_grid(self):
        """returns 1 for a grid of [[1,1,1],[1,1,1],[1,1,1]]"""
        is_connected = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
        actual = number_of_provinces_dfs(is_connected)
        expected = 1
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
