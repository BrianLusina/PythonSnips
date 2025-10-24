import unittest
from . import find_sum_of_three


class FindSumOfThreeTestCases(unittest.TestCase):
    def test_1(self):
        """should return False for nums=[1,-1,0], target=-1"""
        nums = [1, -1, 0]
        target = -1
        actual = find_sum_of_three(nums, target)
        self.assertFalse(actual)

    def test2(self):
        """should return True for nums=[3,7,1,2,8,4,5], target=10"""
        nums = [3,7,1,2,8,4,5]
        target = 10
        actual = find_sum_of_three(nums, target)
        self.assertTrue(actual)

    def test_3(self):
        """should return False for nums=[3,7,1,2,8,4,5], target=21"""
        nums = [3,7,1,2,8,4,5]
        target = 21
        actual = find_sum_of_three(nums, target)
        self.assertFalse(actual)

    def test_4(self):
        """should return True for nums=[-1,2,1,-4,5,-3], target=-8"""
        nums = [-1,2,1,-4,5,-3]
        target = -8
        actual = find_sum_of_three(nums, target)
        self.assertTrue(actual)

    def test_5(self):
        """should return True for nums=[-1,2,1,-4,5,-3], target=0"""
        nums = [-1,2,1,-4,5,-3]
        target = 0
        actual = find_sum_of_three(nums, target)
        self.assertTrue(actual)


if __name__ == '__main__':
    unittest.main()
