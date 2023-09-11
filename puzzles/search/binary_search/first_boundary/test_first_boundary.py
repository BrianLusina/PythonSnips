import unittest
from . import find_boundary


class FindBoundaryTestCase(unittest.TestCase):
    def test_1(self):
        """should return 2 for [false, false, true, true, true]"""
        arr = [False, False, True, True, True]
        expected = 2
        actual = find_boundary(arr)
        self.assertEqual(expected, actual)

    def test_2(self):
        """should return 0 for [True]"""
        arr = [True]
        expected = 0
        actual = find_boundary(arr)
        self.assertEqual(expected, actual)

    def test_3(self):
        """should return -1 for [False, False, False]"""
        arr = [False, False, False]
        expected = -1
        actual = find_boundary(arr)
        self.assertEqual(expected, actual)

    def test_4(self):
        """should return 0 for [True, True, True, True, True]"""
        arr = [True, True, True, True, True]
        expected = 0
        actual = find_boundary(arr)
        self.assertEqual(expected, actual)

    def test_5(self):
        """should return 1 for [False, True]"""
        arr = [False, True]
        expected = 1
        actual = find_boundary(arr)
        self.assertEqual(expected, actual)

    def test_6(self):
        """should return 8 for [False, False, False, False, False, False, False,False, True]"""
        arr = [False, False, False, False, False, False, False, False, True]
        expected = 8
        actual = find_boundary(arr)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
