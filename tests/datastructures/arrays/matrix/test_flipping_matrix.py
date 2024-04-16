import unittest
from datastructures.arrays.matrix.flipping_the_matrix import flipping_matrix


class FlippingTheMatrixTestCase(unittest.TestCase):
    def test_one(self):
        matrix = [
            [112, 42, 83, 119],
            [56, 125, 56, 49],
            [15, 78, 101, 43],
            [62, 98, 114, 108],
        ]
        expected = 414
        actual = flipping_matrix(matrix)
        self.assertEqual(expected, actual)

    def test_two(self):
        matrix = [[1, 2], [3, 4]]
        expected = 4
        actual = flipping_matrix(matrix)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
