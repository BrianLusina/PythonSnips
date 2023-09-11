import unittest

from . import cyclic_rotation, cyclic_rotation_2


class CyclicRotationTestCase(unittest.TestCase):
    def test_1(self):
        """should rotate [1, 10, 20, 0, 59, 86, 32, 11, 9, 40] by n=2"""
        a = [1, 10, 20, 0, 59, 86, 32, 11, 9, 40]
        n = 2
        actual = cyclic_rotation(a, n)
        expected = [9, 40, 1, 10, 20, 0, 59, 86, 32, 11]
        self.assertEqual(expected, actual)

    def test_2(self):
        """should rotate [1, 10, 20, 0, 59, 86, 32, 11, 9, 40] by n=-1"""
        a = [1, 10, 20, 0, 59, 86, 32, 11, 9, 40]
        n = -1
        actual = cyclic_rotation(a, n)
        expected = [10, 20, 0, 59, 86, 32, 11, 9, 40, 1]
        self.assertEqual(expected, actual)

    def test_3(self):
        """should rotate [-1, -100, 3, 99] by n=2"""
        a = [-1, -100, 3, 99]
        n = 2
        actual = cyclic_rotation(a, n)
        expected = [3, 99, -1, -100]
        self.assertEqual(expected, actual)

    def test_4(self):
        """should rotate [1, 2, 3, 4, 5] by n=2"""
        a = [1, 2, 3, 4, 5]
        n = 2
        actual = cyclic_rotation(a, n)
        expected = [4, 5, 1, 2, 3]
        self.assertEqual(expected, actual)

    def test_5(self):
        """should rotate [1, 2, 3, 4, 5, 6, 7] by n=3"""
        a = [1, 2, 3, 4, 5, 6, 7]
        n = 3
        actual = cyclic_rotation(a, n)
        expected = [5, 6, 7, 1, 2, 3, 4]
        self.assertEqual(expected, actual)

    def test_6(self):
        """should rotate [1, 10, 20, 0, 59, 86, 32, 11, 9, 40] by n=-3"""
        a = [1, 10, 20, 0, 59, 86, 32, 11, 9, 40]
        n = -3
        actual = cyclic_rotation(a, n)
        expected = [0, 59, 86, 32, 11, 9, 40, 1, 10, 20]
        self.assertEqual(expected, actual)

    def test_7(self):
        """should rotate [1, 2] by n=1"""
        a = [1, 2]
        n = 1
        actual = cyclic_rotation(a, n)
        expected = [2, 1]
        self.assertEqual(expected, actual)


class CyclicRotation2TestCase(unittest.TestCase):
    def test_1(self):
        """should rotate [1, 10, 20, 0, 59, 86, 32, 11, 9, 40] by n=2"""
        a = [1, 10, 20, 0, 59, 86, 32, 11, 9, 40]
        n = 2
        actual = cyclic_rotation_2(a, n)
        expected = [9, 40, 1, 10, 20, 0, 59, 86, 32, 11]
        self.assertEqual(expected, actual)

    def test_2(self):
        """should rotate [1, 10, 20, 0, 59, 86, 32, 11, 9, 40] by n=-1"""
        a = [1, 10, 20, 0, 59, 86, 32, 11, 9, 40]
        n = -1
        actual = cyclic_rotation_2(a, n)
        expected = [10, 20, 0, 59, 86, 32, 11, 9, 40, 1]
        self.assertEqual(expected, actual)

    def test_3(self):
        """should rotate [-1, -100, 3, 99] by n=2"""
        a = [-1, -100, 3, 99]
        n = 2
        actual = cyclic_rotation_2(a, n)
        expected = [3, 99, -1, -100]
        self.assertEqual(expected, actual)

    def test_4(self):
        """should rotate [1, 2, 3, 4, 5] by n=2"""
        a = [1, 2, 3, 4, 5]
        n = 2
        actual = cyclic_rotation_2(a, n)
        expected = [4, 5, 1, 2, 3]
        self.assertEqual(expected, actual)

    def test_5(self):
        """should rotate [1, 2, 3, 4, 5, 6, 7] by n=3"""
        a = [1, 2, 3, 4, 5, 6, 7]
        n = 3
        actual = cyclic_rotation_2(a, n)
        expected = [5, 6, 7, 1, 2, 3, 4]
        self.assertEqual(expected, actual)

    def test_6(self):
        """should rotate [1, 10, 20, 0, 59, 86, 32, 11, 9, 40] by n=-3"""
        a = [1, 10, 20, 0, 59, 86, 32, 11, 9, 40]
        n = -3
        actual = cyclic_rotation_2(a, n)
        expected = [0, 59, 86, 32, 11, 9, 40, 1, 10, 20]
        self.assertEqual(expected, actual)

    def test_7(self):
        """should rotate [1, 2] by n=1"""
        a = [1, 2]
        n = 1
        actual = cyclic_rotation_2(a, n)
        expected = [2, 1]
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
