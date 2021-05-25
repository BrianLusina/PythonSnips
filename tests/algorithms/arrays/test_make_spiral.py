import unittest

from algorithms.arrays.matrix_in_spiral_form import make_a_spiral


class MakeSpiralTestCase(unittest.TestCase):
    def test_size_5(self):
        size = 5
        expected = [[1, 1, 1, 1, 1],
                    [0, 0, 0, 0, 1],
                    [1, 1, 1, 0, 1],
                    [1, 0, 0, 0, 1],
                    [1, 1, 1, 1, 1]]
        actual = make_a_spiral(size)

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
