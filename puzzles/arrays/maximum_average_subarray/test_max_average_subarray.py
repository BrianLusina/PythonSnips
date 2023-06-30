import unittest

from . import find_max_average


class FindMaxAverageTestCase(unittest.TestCase):
    def test_should_return_12_75000_from_nums_is_1_12__neg5_6_50_3_and_k_is_4(self):
        """should return 12.75000 where nums = [1,12,-5,-6,50,3], k = 4"""
        nums = [1, 12, -5, -6, 50, 3]
        k = 4
        expected = 12.75000
        actual = find_max_average(nums, k)
        self.assertEqual(expected, actual)

    def test_should_return_5_00000_from_nums_is_5_and_k_is_1(self):
        """should return 5.00000 where nums = [5], k = 1"""
        nums = [5]
        k = 1
        expected = 5.00000
        actual = find_max_average(nums, k)
        self.assertEqual(expected, actual)

    def test_should_return_2_00000_from_nums_is_0_1_1_3_3_and_k_is_4(self):
        """should return 2.00000 where nums = [0,1,1,3,3], k = 4"""
        nums = [0, 1, 1, 3, 3]
        k = 4
        expected = 2.00000
        actual = find_max_average(nums, k)
        self.assertEqual(expected, actual)

    def test_should_return_2_80000_from_nums_is_4_0_4_3_3_and_k_is_5(self):
        """should return 2.80000 where nums = [4, 0, 4, 3, 3], k = 5"""
        nums = [4, 0, 4, 3, 3]
        k = 5
        expected = 2.80000
        actual = find_max_average(nums, k)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
