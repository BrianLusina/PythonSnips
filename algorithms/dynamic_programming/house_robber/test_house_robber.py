import unittest
from . import rob


class MyTestCase(unittest.TestCase):
    def test_1(self):
        """should return 4 for nums = [1,2,3,1]"""
        nums = [1, 2, 3, 1]
        expected = 4
        actual = rob(nums)
        self.assertEqual(expected, actual)

    def test_2(self):
        """should return 4 for nums = [2,7,9,3,1]"""
        nums = [2, 7, 9, 3, 1]
        expected = 12
        actual = rob(nums)
        self.assertEqual(expected, actual)

    def test_3(self):
        """should return 0 for nums = []"""
        nums = []
        expected = 0
        actual = rob(nums)
        self.assertEqual(expected, actual)

    def test_4(self):
        """should return 3 for nums = [3]"""
        nums = [3]
        expected = 3
        actual = rob(nums)
        self.assertEqual(expected, actual)

    def test_5(self):
        """should return 3 for nums = [3, 5]"""
        nums = [3, 5]
        expected = 5
        actual = rob(nums)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
