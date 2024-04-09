import unittest
from . import longest_subarray


class LongestSubarrayTestCase(unittest.TestCase):
    def test_one(self):
        """should return 3 from nums = [1,1,0,1]"""
        nums = [1, 1, 0, 1]
        expected = 3
        actual = longest_subarray(nums)
        self.assertEqual(expected, actual)

    def test_two(self):
        """should return 5 from nums = [0,1,1,1,0,1,1,0,1]"""
        nums = [0, 1, 1, 1, 0, 1, 1, 0, 1]
        expected = 5
        actual = longest_subarray(nums)
        self.assertEqual(expected, actual)

    def test_three(self):
        """should return 2 from nums = [1,1,1]"""
        nums = [1, 1, 1]
        expected = 2
        actual = longest_subarray(nums)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
