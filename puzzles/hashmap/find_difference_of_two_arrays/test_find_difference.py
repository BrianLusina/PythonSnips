import unittest
from . import find_difference


class FindDifferenceTestCase(unittest.TestCase):
    def test_one(self):
        """should return [[1,3],[4,6]] from nums1 = [1,2,3], nums2 = [2,4,6]"""
        nums1 = [1, 2, 3]
        nums2 = [2, 4, 6]
        expected = [[1, 3], [4, 6]]
        actual = find_difference(nums1, nums2)
        self.assertEqual(expected, actual)

    def test_two(self):
        """should return [[3],[]] from nums1 = [1,2,3,3], nums2 = [1,1,2,2]"""
        nums1 = [1, 2, 3, 3]
        nums2 = [1, 1, 2, 2]
        expected = [[3], []]
        actual = find_difference(nums1, nums2)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
