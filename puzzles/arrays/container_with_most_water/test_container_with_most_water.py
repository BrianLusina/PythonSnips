import unittest

from . import max_area


class ContainerWithMostWaterTestCases(unittest.TestCase):
    def test_one(self):
        """should return 49 from height=[1,8,6,2,5,4,8,3,7]"""
        height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
        expected = 49
        actual = max_area(height)
        self.assertEqual(expected, actual)

    def test_two(self):
        """should return 1 from height=[1,1]"""
        height = [1, 1]
        expected = 1
        actual = max_area(height)
        self.assertEqual(expected, actual)

    def test_three(self):
        """should return 6 from height=[1,5, 4, 3]"""
        height = [1, 5, 4, 3]
        expected = 6
        actual = max_area(height)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
