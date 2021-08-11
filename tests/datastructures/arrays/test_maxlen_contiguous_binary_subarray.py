import unittest

from datastructures.arrays.maxlen_contiguous_binary_subarray import find_max_length


class MaxLengthContiguousBinarySubArrayTestCases(unittest.TestCase):
    def test_0_1(self):
        nums = [0, 1]
        expected = 2
        actual = find_max_length(nums)
        self.assertEqual(expected, actual)

    def test_0_1_0(self):
        nums = [0, 1, 0]
        expected = 2
        actual = find_max_length(nums)
        self.assertEqual(expected, actual)

    def test_0_1_0_0_1_1_0(self):
        nums = [0, 1, 0, 0, 1, 1, 0]
        expected = 6
        actual = find_max_length(nums)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
