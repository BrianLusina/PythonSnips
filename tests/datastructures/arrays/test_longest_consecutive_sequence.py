import unittest

from datastructures.arrays.longest_consecutive_sequence import longest_consecutive


class LongestConsecutiveSequenceTestCases(unittest.TestCase):
    def test_100_4_200_1_3_2_returns_4(self):
        """should return 4 from nums = [100,4,200,1,3,2]"""
        nums = [100, 4, 200, 1, 3, 2]
        expected = 4
        actual = longest_consecutive(nums)
        self.assertEqual(expected, actual)

    def test_0_3_7_2_5_8_4_6_0_1_returns_9(self):
        """should return 9 from nums = [0,3,7,2,5,8,4,6,0,1]"""
        nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
        expected = 9
        actual = longest_consecutive(nums)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
