import unittest

from algorithms.arrays.matrix_in_spiral_form import generate_n_by_n_matrix_in_spiral_form


class MatrixInSpiralFormTestCase(unittest.TestCase):
    def test_n_is_3(self):
        n = 3
        expected = [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
        actual = generate_n_by_n_matrix_in_spiral_form(n)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
