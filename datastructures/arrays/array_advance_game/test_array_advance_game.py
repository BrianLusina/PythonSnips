import unittest
from . import array_advance


class ArrayAdvanceGameTestCase(unittest.TestCase):
    def test_1(self):
        """should return true for [3, 3, 1, 0, 2, 0, 1]"""
        a = [3, 3, 1, 0, 2, 0, 1]
        actual = array_advance(a)
        self.assertTrue(actual)

    def test_2(self):
        """should return false for [3, 2, 0, 0, 2, 0, 1]"""
        a = [3, 2, 0, 0, 2, 0, 1]
        actual = array_advance(a)
        self.assertFalse(actual)

    def test_3(self):
        """should return true for [1, 4, 1, 1, 0, 2, 3]"""
        a = [1, 4, 1, 1, 0, 2, 3]
        actual = array_advance(a)
        self.assertTrue(actual)


if __name__ == '__main__':
    unittest.main()
