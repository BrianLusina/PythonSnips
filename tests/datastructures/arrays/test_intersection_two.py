import unittest

from datastructures.arrays.intersection_of_two_arrays.intersection_two import intersect


class IntersectionTwoTestCase(unittest.TestCase):
    def test_1_2_2_1_and_2_2_returns_2_2(self):
        """Should return [2, 2] for nums1=[1,2,2,1] and nums2=[2,2]"""
        nums1 = [1, 2, 2, 1]
        nums2 = [2, 2]
        expected = [2, 2]
        self.assertEqual(intersect(nums1, nums2), expected)

    def test_4_9_5_and_9_4_9_8_4_returns_4_9(self):
        """Should return [4, 9] for nums1=[4,9,5] and nums2=[9,4,9,8,4]"""
        nums1 = [4, 9, 5]
        nums2 = [9, 4, 9, 8, 4]
        expected = [4, 9]
        self.assertEqual(intersect(nums1, nums2), expected)


if __name__ == '__main__':
    unittest.main()
