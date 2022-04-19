import unittest

from datastructures.arrays.intersection_of_two_arrays.intersection_one import (
    intersection,
)


class IntersectionArraysTestCase(unittest.TestCase):
    def test_1_2_2_1_and_2_2(self):
        nums1 = [1, 2, 2, 1]
        nums2 = [2, 2]
        expected = [2]
        actual = intersection(nums1, nums2)
        self.assertEqual(actual, expected)

    def test_4_9_5_and_9_4_9_8_4(self):
        nums1 = [4, 9, 5]
        nums2 = [9, 4, 9, 8, 4]
        expected = [9, 4]
        actual = intersection(nums1, nums2)
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
