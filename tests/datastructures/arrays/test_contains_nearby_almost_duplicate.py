import unittest

from datastructures.arrays.contains_duplicates import contains_nearby_almost_duplicate


class ContainsNearbyDuplicateTestCases(unittest.TestCase):
    def test_nums_is_1_2_3_1_and_k_is_3_and_t_is_0(self):
        """Should return true for nums=[1,2,3,1] and k = 3 and t = 0"""
        nums = [1, 2, 3, 1]
        k = 3
        t = 0
        actual = contains_nearby_almost_duplicate(nums, k, t)
        self.assertTrue(actual)

    def test_nums_is_1_0_1_1_and_k_is_1_and_t_is_2(self):
        """Should return true for nums=[1,0,1,1] and k = 1 and t = 2"""
        nums = [1, 0, 1, 1]
        k = 1
        t = 2
        actual = contains_nearby_almost_duplicate(nums, k, t)
        self.assertTrue(actual)

    def test_nums_is_1_5_9_1_5_9_and_k_is_2_and_t_is_3(self):
        """Should return false for nums=[1,2,3,1,2,3] and k = 2 and t = 3"""
        nums = [1, 5, 9, 1, 5, 9]
        k = 2
        t = 3
        actual = contains_nearby_almost_duplicate(nums, k, t)
        self.assertFalse(actual)


if __name__ == '__main__':
    unittest.main()
