import unittest
from . import set_matrix_zeros


class SetMatrixZeroTestCase(unittest.TestCase):
    def test_1(self):
        matrix = [[1,2,3],[4,5,6],[7,0,9]]
        expected = [[1,0,3],[4,0,6],[0,0,0]]
        actual = set_matrix_zeros(matrix)
        self.assertEqual(expected, actual)

    def test_2(self):
        matrix = [[1,2,3,4],[4,5,6,7],[8,9,4,6]]
        expected = [[1,2,3,4],[4,5,6,7],[8,9,4,6]]
        actual = set_matrix_zeros(matrix)
        self.assertEqual(expected, actual)

    def test_3(self):
        matrix = [[1,1,0,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,0,1,1,1],[1,1,1,1,1]]
        expected = [[0, 0, 0, 0, 0], [1, 0, 0, 1, 1], [1, 0, 0, 1, 1], [0, 0, 0, 0, 0], [1, 0, 0, 1, 1]]
        actual = set_matrix_zeros(matrix)
        self.assertEqual(expected, actual)

    def test_4(self):
        matrix = [[1,1,1],[1,0,1],[1,1,1]]
        expected = [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
        actual = set_matrix_zeros(matrix)
        self.assertEqual(expected, actual)

    def test_5(self):
        matrix = [[3,5,2,0],[1,0,4,6],[7,3,2,4]]
        expected = [[0, 0, 0, 0], [0, 0, 0, 0], [7, 0, 2, 0]]
        actual = set_matrix_zeros(matrix)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
