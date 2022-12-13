import unittest

from algorithms.binary_search.min_in_rotated_sorted_array import find_min


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


if __name__ == '__main__':
    unittest.main()
