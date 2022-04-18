import unittest

from datastructures.arrays.max_subarray import find_max_sub_array


class MaxSubArrayTestCases(unittest.TestCase):
    def test_empty_array(self):
        nums = []
        expected = 0
        actual = find_max_sub_array(nums)
        self.assertEqual(expected, actual)

    def test_single_element_array(self):
        nums = [1]
        expected = 1
        actual = find_max_sub_array(nums)
        self.assertEqual(expected, actual)

    def test_2_1_3_4_1_2_1_5_4(self):
        nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        expected = 6
        actual = find_max_sub_array(nums)
        self.assertEqual(expected, actual)

    def test_5_4_1_7_8(self):
        nums = [5, 4, -1, 7, 8]
        expected = 23
        actual = find_max_sub_array(nums)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
