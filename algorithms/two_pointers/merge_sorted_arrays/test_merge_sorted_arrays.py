import unittest

from . import merge


class MergeSortedArraysTestCases(unittest.TestCase):
    def test_should_return_0_when_empty_array(self):
        nums1 = []
        nums2 = []
        merge(nums1, 0, nums2, 0)
        self.assertEqual(nums1, [])

    def test_set_nums1_to_1_2_2_3_5_6_when_nums1_is_1_2_3_0_0_0_and_m_is_3_and_nums2_is_2_5_6_and_n_is_3(
            self,
    ):
        """Should set nums1 to [1,2,2,3,5,6] when initially nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3"""
        nums1 = [1, 2, 3, 0, 0, 0]
        m = 3
        nums2 = [2, 5, 6]
        n = 3
        merge(nums1, m, nums2, n)
        expected = [1, 2, 2, 3, 5, 6]
        self.assertEqual(nums1, expected)

    def test_set_nums1_to_1_when_nums1_is_0_and_m_is_0_and_nums2_is_1_and_n_is_1(self):
        """Should set nums1 to [1] when initially nums1 = [0], m = 0, nums2 = [1], n = 1"""
        nums1 = [0]
        m = 0
        nums2 = [1]
        n = 1
        expected = [1]
        merge(nums1, m, nums2, n)
        self.assertEqual(nums1, expected)
