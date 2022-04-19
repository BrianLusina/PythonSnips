import unittest

from datastructures.arrays.matrix.reshape_matrix import (
    matrix_reshape,
    matrix_reshape_2,
    matrix_reshape_3,
)


class ReshapeMatrixTestCases(unittest.TestCase):
    def test_should_return_1_2_3_4_for_r_1_and_c_4(self):
        """Should return [[1,2,3,4]] for input[[1,2],[3,4]] and r=1 and c=4"""
        matrix = [[1, 2], [3, 4]]
        r = 1
        c = 4
        expected_matrix = [[1, 2, 3, 4]]
        self.assertEqual(expected_matrix, matrix_reshape(matrix, r, c))

    def test_should_return_original_matrix_if_reshape_can_not_happen_for_r_2_and_c_4(
        self,
    ):
        """Should return [[1,2],[3,4]] for input[[1,2],[3,4]] and r=2 and c=4"""
        matrix = [[1, 2], [3, 4]]
        r = 2
        c = 4
        expected_matrix = [[1, 2], [3, 4]]
        self.assertEqual(expected_matrix, matrix_reshape(matrix, r, c))

    def test_should_return_1_2_3_4_for_r_1_and_c_4_with_matrix_reshape_2(self):
        """Should return [[1,2,3,4]] for input[[1,2],[3,4]] and r=1 and c=4 for matrix_reshape_2"""
        matrix = [[1, 2], [3, 4]]
        r = 1
        c = 4
        expected_matrix = [[1, 2, 3, 4]]
        self.assertEqual(expected_matrix, matrix_reshape_2(matrix, r, c))

    def test_should_return_original_matrix_if_reshape_can_not_happen_for_r_2_and_c_4_with_matrix_reshape_2(
        self,
    ):
        """Should return [[1,2],[3,4]] for input[[1,2],[3,4]] and r=2 and c=4 for matrix_reshape_2"""
        matrix = [[1, 2], [3, 4]]
        r = 2
        c = 4
        expected_matrix = [[1, 2], [3, 4]]
        self.assertEqual(expected_matrix, matrix_reshape_2(matrix, r, c))

    def test_should_return_1_2_3_4_for_r_1_and_c_4_with_matrix_reshape_3(self):
        """Should return [[1,2,3,4]] for input[[1,2],[3,4]] and r=1 and c=4 for matrix_reshape_3"""
        matrix = [[1, 2], [3, 4]]
        r = 1
        c = 4
        expected_matrix = [[1, 2, 3, 4]]
        self.assertEqual(expected_matrix, matrix_reshape_3(matrix, r, c))

    def test_should_return_original_matrix_if_reshape_can_not_happen_for_r_2_and_c_4_with_matrix_reshape_3(
        self,
    ):
        """Should return [[1,2],[3,4]] for input[[1,2],[3,4]] and r=2 and c=4 for matrix_reshape_3"""
        matrix = [[1, 2], [3, 4]]
        r = 2
        c = 4
        expected_matrix = [[1, 2], [3, 4]]
        self.assertEqual(expected_matrix, matrix_reshape_3(matrix, r, c))


if __name__ == "__main__":
    unittest.main()
