import unittest
from . import plates_between_candles


class PlatesBetweenCandlesTestCase(unittest.TestCase):
    def test_1(self):
        """should return [2,3] from s = "**|**|***|", queries = [[2,5],[5,9]]"""
        s = "**|**|***|"
        queries = [[2, 5], [5, 9]]
        expected = [2, 3]
        actual = plates_between_candles(s, queries)

        self.assertEqual(expected, actual)

    def test_2(self):
        """should return [9, 0, 0, 0, 0] from s = "***|**|*****|**||**|*", queries = [[1,17],[4,5],[14,17],[5,11],[15,16]]"""
        s = "***|**|*****|**||**|*"
        queries = [[1, 17], [4, 5], [14, 17], [5, 11], [15, 16]]
        expected = [9, 0, 0, 0, 0]
        actual = plates_between_candles(s, queries)

        self.assertEqual(expected, actual)

    def test_3(self):
        """should return [9, 0, 0, 0, 0] from s = "||**||**|*", queries = [[3,8]]"""
        s = "||**||**|*"
        queries = [[3, 8]]
        expected = [2]
        actual = plates_between_candles(s, queries)

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
