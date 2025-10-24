import unittest

from . import longest_ones


class MaxConsecutiveOnesTestCase(unittest.TestCase):
    def test_one(self):
        """should return 6 from nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2"""
        nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
        k = 2
        expected = 6
        actual = longest_ones(nums, k)
        self.assertEqual(expected, actual)

    def test_two(self):
        """should return 10 from nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3"""
        nums = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
        k = 3
        expected = 10
        actual = longest_ones(nums, k)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
