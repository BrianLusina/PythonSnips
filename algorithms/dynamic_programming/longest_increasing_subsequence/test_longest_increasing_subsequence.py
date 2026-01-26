import unittest

from . import longest_increasing_subsequence


class LongestIncreasingSubsequenceTestCase(unittest.TestCase):
    def test_1(self):
        """should return 3 from input of [1, 2, 1, 5]"""
        nums = [1, 2, 1, 5]
        expected = 3
        actual = longest_increasing_subsequence(nums)
        self.assertEqual(expected, actual)

    def test_2(self):
        """should return 6 from input of [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]"""
        nums = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
        expected = 6
        actual = longest_increasing_subsequence(nums)
        self.assertEqual(expected, actual)

    def test_3(self):
        """should return 3 from input of [3, 10, 2, 1, 20]"""
        nums = [3, 10, 2, 1, 20]
        expected = 3
        actual = longest_increasing_subsequence(nums)
        self.assertEqual(expected, actual)

    def test_4(self):
        """should return 1 from input of [3, 2]"""
        nums = [3, 2]
        expected = 1
        actual = longest_increasing_subsequence(nums)
        self.assertEqual(expected, actual)

    def test_5(self):
        """should return 4 from input of [50, 3, 10, 7, 40, 80]"""
        nums = [50, 3, 10, 7, 40, 80]
        expected = 4
        actual = longest_increasing_subsequence(nums)
        self.assertEqual(expected, actual)

    def test_6(self):
        """should return 4 from input of [10,9,2,5,3,7,101,18]"""
        nums = [10, 9, 2, 5, 3, 7, 101, 18]
        expected = 4
        actual = longest_increasing_subsequence(nums)
        self.assertEqual(expected, actual)

    def test_7(self):
        """should return 4 from input of [0,1,0,3,2,3]"""
        nums = [0, 1, 0, 3, 2, 3]
        expected = 4
        actual = longest_increasing_subsequence(nums)
        self.assertEqual(expected, actual)

    def test_8(self):
        """should return 4 from input of [7,7,7,7,7,7,7]"""
        nums = [7, 7, 7, 7, 7, 7, 7]
        expected = 1
        actual = longest_increasing_subsequence(nums)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
