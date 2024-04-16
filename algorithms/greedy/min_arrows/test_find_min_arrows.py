import unittest
from . import find_min_arrow_shots


class FindMinArrowShotsTestCase(unittest.TestCase):
    def test_1(self):
        """points = [[10,16],[2,8],[1,6],[7,12]] should return 2"""
        points = [[10, 16], [2, 8], [1, 6], [7, 12]]
        expected = 2
        actual = find_min_arrow_shots(points)
        self.assertEqual(expected, actual)

    def test_2(self):
        """points = [[1,2],[3,4],[5,6],[7,8]] should return 4"""
        points = [[1, 2], [3, 4], [5, 6], [7, 8]]
        expected = 4
        actual = find_min_arrow_shots(points)
        self.assertEqual(expected, actual)

    def test_3(self):
        """points = [[1,2],[2,3],[3,4],[4,5]] should return 2"""
        points = [[1, 2], [2, 3], [3, 4], [4, 5]]
        expected = 2
        actual = find_min_arrow_shots(points)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
