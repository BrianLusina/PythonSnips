import unittest

from . import intersection


class IntersectionTestCases(unittest.TestCase):
    def test_1(self):
        """should return [3,4] for a = [3,1,4,2], b = [4,5,3,6]"""
        a = [3, 1, 4, 2]
        b = [4, 5, 3, 6]
        expected = [3, 4]
        actual = intersection(a, b)
        self.assertEqual(expected, actual)

    def test_2(self):
        """should return [3,7] for a = [2,3,3,5,7,11], b = [3,3,7,15,31]"""
        a = [2, 3, 3, 5, 7, 11]
        b = [3, 3, 7, 15, 31]
        expected = [3, 3, 7]
        actual = intersection(a, b)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
