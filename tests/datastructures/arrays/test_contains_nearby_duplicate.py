import unittest


from datastructures.arrays.contains_duplicates import contains_nearby_duplicate


class ContainsNearbyDuplicateTestCases(unittest.TestCase):
    def test_nums_is_1_2_3_1_and_k_is_3(self):
        """Should return true for nums=[1,2,3,1] and k = 3"""
        nums = [1, 2, 3, 1]
        k = 3
        expected = True
        actual = contains_nearby_duplicate(nums, k)
        self.assertEqual(expected, actual)

    def test_nums_is_1_0_1_1_and_k_is_1(self):
        """Should return true for nums=[1,0,1,1] and k = 1"""
        nums = [1, 0, 1, 1]
        k = 1
        expected = True
        actual = contains_nearby_duplicate(nums, k)
        self.assertEqual(expected, actual)

    def test_nums_is_1_2_3_1_2_3_and_k_is_2(self):
        """Should return false for nums=[1,2,3,1,2,3] and k = 2"""
        nums = [1,2,3,1,2,3]
        k = 2
        expected = False
        actual = contains_nearby_duplicate(nums, k)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
