import unittest

from datastructures.arrays.matrix.diagonal_difference import diagonal_difference


class DiagonalDifferenceTestCases(unittest.TestCase):
    def test_1_2_3_4_5_6_9_8_9_returns_2(self):
        """matrix of [[1,2,3],[4,5,6],[9,8,9]] should return 2"""
        arr = [[1, 2, 3], [4, 5, 6], [9, 8, 9]]
        expected = 2
        actual = diagonal_difference(arr)
        self.assertEqual(expected, actual)

    def test_11_2_4_4_5_6_10_8_neg12_returns_2(self):
        """matrix of [[11,2,4],[4,5,6],[10,8,-12]] should return 15"""
        arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
        expected = 15
        actual = diagonal_difference(arr)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
