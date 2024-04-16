import unittest

from . import find_min


class TestFinMinInRotatedSortedArray(unittest.TestCase):
    def test_nums_3_4_5_1_2(self):
        """Should return 1 from nums = [3,4,5,1,2]"""
        nums = [3, 4, 5, 1, 2]
        expected = 1
        actual = find_min(nums)
        self.assertEqual(expected, actual)

    def test_nums_4_5_6_7_0_1_2(self):
        """Should return 0 from nums = [4,5,6,7,0,1,2]"""
        nums = [4, 5, 6, 7, 0, 1, 2]
        expected = 0
        actual = find_min(nums)
        self.assertEqual(expected, actual)

    def test_nums_11_13_15_17(self):
        """Should return 11 from nums = [11,13,15,17]"""
        nums = [11, 13, 15, 17]
        expected = 11
        actual = find_min(nums)
        self.assertEqual(expected, actual)

    def test_nums_30_40_50_10_20(self):
        """Should return 11 from nums = [30, 40, 50, 10, 20]"""
        nums = [30, 40, 50, 10, 20]
        expected = 10
        actual = find_min(nums)
        self.assertEqual(expected, actual)

    def test_nums_3_5_7_11_13_17_19_2(self):
        """Should return 2 from nums = [3, 5, 7, 11, 13, 17, 19, 2]"""
        nums = [3, 5, 7, 11, 13, 17, 19, 2]
        expected = 2
        actual = find_min(nums)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
