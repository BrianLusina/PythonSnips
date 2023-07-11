import unittest

from . import pivot_index


class PivotIndexTestCases(unittest.TestCase):
    def test_one(self):
        """should return 3 from nums=[1,7,3,6,5,6]"""
        nums = [1, 7, 3, 6, 5, 6]
        expected = 3
        actual = pivot_index(nums)
        self.assertEqual(expected, actual)

    def test_two(self):
        """should return -1 from nums=[1,2,3]"""
        nums = [1, 2, 3]
        expected = -1
        actual = pivot_index(nums)
        self.assertEqual(expected, actual)

    def test_three(self):
        """should return 0 from nums=[2,1,-1]"""
        nums = [2, 1, -1]
        expected = 0
        actual = pivot_index(nums)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
