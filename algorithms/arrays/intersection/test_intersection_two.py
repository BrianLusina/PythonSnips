import unittest

from algorithms.arrays.intersection.intersection_two import intersect


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

    def test_2(self):
        """should return [3,3,7] for a = [2,3,3,5,7,11], b = [3,3,7,15,31]"""
        a = [2, 3, 3, 5, 7, 11]
        b = [3, 3, 7, 15, 31]
        expected = [3, 3, 7]
        actual = intersect(a, b)
        self.assertEqual(expected, actual)

    def test_2_remove_duplicates(self):
        """should return [3,7] for a = [2,3,3,5,7,11], b = [3,3,7,15,31] without including duplicates"""
        a = [2, 3, 3, 5, 7, 11]
        b = [3, 3, 7, 15, 31]
        expected = [3, 7]
        actual = intersect(a, b, include_duplicates=False)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
