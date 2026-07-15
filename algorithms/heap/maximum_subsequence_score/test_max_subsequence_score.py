import unittest

from . import max_score


class MaxSubsequenceScoreTestCase(unittest.TestCase):
    def test_1(self):
        """nums1 = [1,3,3,2], nums2 = [2,1,3,4], k = 3 returns 12"""
        nums1 = [1, 3, 3, 2]
        nums2 = [2, 1, 3, 4]
        k = 3
        expected = 12
        actual = max_score(nums1, nums2, k)
        self.assertEqual(expected, actual)

    def test_2(self):
        """nums1 = [4,2,3,1,1], nums2 = [7,5,10,9,6], k = 1 returns 30"""
        nums1 = [4, 2, 3, 1, 1]
        nums2 = [7, 5, 10, 9, 6]
        k = 1
        expected = 30
        actual = max_score(nums1, nums2, k)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
