import unittest

from . import search, search_with_duplicates


class SearchRotatedSortedArrayTestCases(unittest.TestCase):
    def test_nums_4_5_6_7_0_1_2_and_target_0(self):
        """nums = [4,5,6,7,0,1,2] and target = 0 returns 4"""
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 0
        expected = 4
        actual = search(nums, target)
        self.assertEqual(expected, actual)

    def test_nums_4_5_6_7_0_1_2_and_target_3(self):
        """nums = [4,5,6,7,0,1,2] and target = 3 returns -1"""
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 3
        expected = -1
        actual = search(nums, target)
        self.assertEqual(expected, actual)

    def test_nums_4_5_6_7_0_1_2_3_and_target_4(self):
        """nums = [4,5,6,7,0,1,2,3] and target = 4 returns 0"""
        nums = [4, 5, 6, 7, 0, 1, 2, 3]
        target = 4
        expected = 0
        actual = search(nums, target)
        self.assertEqual(expected, actual)

    def test_nums_5_17_100_3_and_target_6(self):
        """nums = [5,17,100,3] and target = 6 returns -1"""
        nums = [5, 17, 100, 3]
        target = 6
        expected = -1
        actual = search(nums, target)
        self.assertEqual(expected, actual)

    def test_nums_1_and_target_0(self):
        """nums = [1] and target = 0 returns -1"""
        nums = [1]
        target = 0
        expected = -1
        actual = search(nums, target)
        self.assertEqual(expected, actual)


class SearchRotatedSortedArrayWithDuplicatesTestCases(unittest.TestCase):
    def test_nums_2_5_6_0_0_1_2_and_target_0(self):
        """nums = [2,5,6,0,0,1,2] and target = 0 returns true"""
        nums = [2, 5, 6, 0, 0, 1, 2]
        target = 0
        actual = search_with_duplicates(nums, target)
        self.assertTrue(actual)

    def test_nums_2_5_6_0_0_1_2_and_target_3(self):
        """nums = [2,5,6,0,0,1,2] and target = 3 returns false"""
        nums = [2, 5, 6, 0, 0, 1, 2]
        target = 3
        actual = search_with_duplicates(nums, target)
        self.assertFalse(actual)

    def test_nums_4_5_6_6_7_0_1_2_4_4_and_target_3(self):
        """nums = [4,5,6,6,7,0,1,2,4,4] and target = 6 returns true"""
        nums = [4, 5, 6, 6, 7, 0, 1, 2, 4, 4]
        target = 6
        actual = search_with_duplicates(nums, target)
        self.assertTrue(actual)

    def test_nums_1_0_1_1_1_and_target_0(self):
        """nums = [1,0,1,1,1] and target = 0 returns true"""
        nums = [1, 0, 1, 1, 1]
        target = 0
        actual = search_with_duplicates(nums, target)
        self.assertTrue(actual)

    def test_nums_1_3_5_and_target_1(self):
        """nums = [1,3,5] and target = 1 returns true"""
        nums = [1, 3, 5]
        target = 1
        actual = search_with_duplicates(nums, target)
        self.assertTrue(actual)


if __name__ == "__main__":
    unittest.main()
