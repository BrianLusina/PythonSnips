import unittest
from . import find_fixed_point, find_fixed_point_linear


class FindFixedPointTestCase(unittest.TestCase):
    def test_fixed_point_1(self):
        """should return 3 as the fixed point for [-10, -5, 0, 3, 7]"""
        numbers = [-10, -5, 0, 3, 7]
        expected = 3
        actual = find_fixed_point(numbers)
        self.assertEqual(expected, actual)

    def test_fixed_point_linear_1(self):
        """should return 3 as the fixed point for [-10, -5, 0, 3, 7]"""
        numbers = [-10, -5, 0, 3, 7]
        expected = 3
        actual = find_fixed_point_linear(numbers)
        self.assertEqual(expected, actual)

    def test_fixed_point_2(self):
        """should return 3 as the fixed point for [0, 2, 5, 8, 17]"""
        numbers = [0, 2, 5, 8, 17]
        expected = 0
        actual = find_fixed_point(numbers)
        self.assertEqual(expected, actual)

    def test_fixed_point_linear_2(self):
        """should return 3 as the fixed point for [0, 2, 5, 8, 17]"""
        numbers = [0, 2, 5, 8, 17]
        expected = 0
        actual = find_fixed_point_linear(numbers)
        self.assertEqual(expected, actual)

    def test_fixed_point_3(self):
        """should return None for no fixed point of [-10, -5, 3, 4, 7, 9]"""
        numbers = [-10, -5, 3, 4, 7, 9]
        actual = find_fixed_point(numbers)
        self.assertIsNone(actual)

    def test_fixed_point_linear_3(self):
        """should return None for no fixed point of [-10, -5, 3, 4, 7, 9]"""
        numbers = [-10, -5, 3, 4, 7, 9]
        actual = find_fixed_point_linear(numbers)
        self.assertIsNone(actual)


if __name__ == "__main__":
    unittest.main()
