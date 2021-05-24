import unittest

from algorithms.arrays.matrix_in_spiral_form import matrix_in_spiral_form


class MatrixInSpiralFormTestCase(unittest.TestCase):
    def test_1_2_3_4_5_6_7_8_9(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        expected = [1, 2, 3, 6, 9, 8, 7, 4, 5]
        actual = matrix_in_spiral_form(matrix)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
