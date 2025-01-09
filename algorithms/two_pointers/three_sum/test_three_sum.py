import unittest

from algorithms.two_pointers.three_sum import three_sum


class ThreeSumTestCases(unittest.TestCase):
    def test_one(self):
        """Should return [[-1, -1, 2], [-1, 0, 1]] for nums = [-1, 0, 1, 2, -1, -4]"""
        nums = [-1, 0, 1, 2, -1, -4]
        expected = [[-1, -1, 2], [-1, 0, 1]]
        actual = three_sum(nums)
        self.assertEqual(expected, actual)

    def test_two(self):
        """Should return [] for nums = [0, 1, 1]"""
        nums = [0, 1, 1]
        expected = []
        actual = three_sum(nums)
        self.assertEqual(expected, actual)

    def test_three(self):
        """Should return [[0,0,0]] for nums = [0,0,0]"""
        nums = [0, 0, 0]
        expected = [[0, 0, 0]]
        actual = three_sum(nums)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
