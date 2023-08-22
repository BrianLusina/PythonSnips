import unittest

from . import minimize_absolute_difference


class MinimizeAbsoluteDifferenceTestCase(unittest.TestCase):
    def test_1(self):
        """a = [1, 4, 5, 8, 10], b=[6, 9, 15 ], c = [2, 3, 6, 6] should return 1"""
        a = [1, 4, 5, 8, 10]
        b = [6, 9, 15]
        c = [2, 3, 6, 6]
        expected = 1
        actual = minimize_absolute_difference(a, b, c)

        self.assertEqual(expected, actual)

    def test_2(self):
        """a = [5, 8, 10, 15], b=[6, 9, 15, 78, 89], c = [2, 3, 6, 6, 8, 8, 10] should return 1"""
        a = [5, 8, 10, 15]
        b = [6, 9, 15, 78, 89]
        c = [2, 3, 6, 6, 8, 8, 10]
        expected = 1
        actual = minimize_absolute_difference(a, b, c)

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
