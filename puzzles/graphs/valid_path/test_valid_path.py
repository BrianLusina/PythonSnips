import unittest
from . import valid_path


class ValidPathTestCases(unittest.TestCase):
    def test_1(self):
        """should return False for x = 2, y = 3, circles = 1, radius = 1, x_coordinates = [2], y_coordinates = [3]"""
        x = 2
        y = 3
        circles = 1
        radius = 1
        x_coordinates = [2]
        y_coordinates = [3]
        actual = valid_path(x, y, circles, radius, x_coordinates, y_coordinates)
        self.assertFalse(actual)

    def test_2(self):
        """should return True for x = 5, y = 5, circles = 2, radius = 1, x_coordinates = [1, 3], y_coordinates = [3,3]"""
        x = 5
        y = 5
        circles = 2
        radius = 1
        x_coordinates = [1, 3]
        y_coordinates = [3, 3]
        actual = valid_path(x, y, circles, radius, x_coordinates, y_coordinates)
        self.assertTrue(actual)

    def test_3(self):
        """should return True for x = 5, y = 5, circles = 2, radius = 1, x_coordinates = [1, 1], y_coordinates = [2,3]"""
        x = 5
        y = 5
        circles = 2
        radius = 1
        x_coordinates = [1, 1]
        y_coordinates = [2, 3]
        actual = valid_path(x, y, circles, radius, x_coordinates, y_coordinates)
        self.assertTrue(actual)

    def test_4(self):
        """should return False for x = 0, y = 91, circles = 3, radius = 5, x_coordinates = [0, 0, 0], y_coordinates = [21, 20, 43]"""
        x = 0
        y = 91
        circles = 3
        radius = 5
        x_coordinates = [0, 0, 0]
        y_coordinates = [21, 20, 43]
        actual = valid_path(x, y, circles, radius, x_coordinates, y_coordinates)
        self.assertFalse(actual)

    def test_5(self):
        """should return False for x = 77, y = 0, circles = 9, radius = 9, x_coordinates = [41, 46, 13, 62, 3, 38, 53, 67, 67], y_coordinates = [0, 0, 0, 0, 0, 0, 0, 0, 0]"""
        x = 77
        y = 0
        circles = 9
        radius = 9
        x_coordinates = [41, 46, 13, 62, 3, 38, 53, 67, 67]
        y_coordinates = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        actual = valid_path(x, y, circles, radius, x_coordinates, y_coordinates)
        self.assertFalse(actual)

    def test_6(self):
        """should return True for x = 37, y = 38, circles = 9, radius = 2, x_coordinates = [15, 11, 7, 31, 3, 18, 18, 12, 31], y_coordinates = [5, 5, 0, 29, 2, 14, 1, 30, 18]"""
        x = 37
        y = 38
        circles = 9
        radius = 2
        x_coordinates = [15, 11, 7, 31, 3, 18, 18, 12, 31]
        y_coordinates = [5, 5, 0, 29, 2, 14, 1, 30, 18]
        actual = valid_path(x, y, circles, radius, x_coordinates, y_coordinates)
        self.assertTrue(actual)


if __name__ == '__main__':
    unittest.main()
