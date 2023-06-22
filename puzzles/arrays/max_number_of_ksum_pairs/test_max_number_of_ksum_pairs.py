import unittest

from . import max_operations, max_operations_with_hashmap


class MaxNumberOfKSumPairsTestCase(unittest.TestCase):
    def test_nums_1_2_3_4_and_k_is_5(self):
        """should return 2 for nums = [1,2,3,4] and k = 5"""
        nums = [1, 2, 3, 4]
        expected = 2
        k = 5
        actual = max_operations(nums=nums, k=k)

        self.assertEqual(expected, actual)

    def test_nums_3_1_3_4_3_and_k_is_6(self):
        """should return 1 for nums = [3,1,3,4,3] and k = 6"""
        nums = [3, 1, 3, 4, 3]
        k = 6
        expected = 1
        actual = max_operations(nums=nums, k=k)

        self.assertEqual(expected, actual)

    def test_nums_4_4_1_3_1_3_2_2_5_5_1_5_2_1_2_3_5_4_and_k_is_2(self):
        """should return 2 for nums = [4,4,1,3,1,3,2,2,5,5,1,5,2,1,2,3,5,4] and k = 2"""
        nums = [4, 4, 1, 3, 1, 3, 2, 2, 5, 5, 1, 5, 2, 1, 2, 3, 5, 4]
        k = 2
        expected = 2
        actual = max_operations(nums=nums, k=k)

        self.assertEqual(expected, actual)


class MaxNumberOfKSumPairsWithHashMapTestCase(unittest.TestCase):
    def test_nums_1_2_3_4_and_k_is_5(self):
        """should return 2 for nums = [1,2,3,4] and k = 5"""
        nums = [1, 2, 3, 4]
        expected = 2
        k = 5
        actual = max_operations_with_hashmap(nums=nums, k=k)

        self.assertEqual(expected, actual)

    def test_nums_3_1_3_4_3_and_k_is_6(self):
        """should return 1 for nums = [3,1,3,4,3] and k = 6"""
        nums = [3, 1, 3, 4, 3]
        k = 6
        expected = 1
        actual = max_operations_with_hashmap(nums=nums, k=k)

        self.assertEqual(expected, actual)

    def test_nums_4_4_1_3_1_3_2_2_5_5_1_5_2_1_2_3_5_4_and_k_is_2(self):
        """should return 2 for nums = [4,4,1,3,1,3,2,2,5,5,1,5,2,1,2,3,5,4] and k = 2"""
        nums = [4, 4, 1, 3, 1, 3, 2, 2, 5, 5, 1, 5, 2, 1, 2, 3, 5, 4]
        k = 2
        expected = 2
        actual = max_operations_with_hashmap(nums=nums, k=k)

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
