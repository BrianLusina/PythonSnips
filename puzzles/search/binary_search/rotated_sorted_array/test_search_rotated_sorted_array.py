import unittest

from . import search


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

    def test_nums_1_and_target_0(self):
        """nums = [1] and target = 0 returns -1"""
        nums = [1]
        target = 0
        expected = -1
        actual = search(nums, target)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
