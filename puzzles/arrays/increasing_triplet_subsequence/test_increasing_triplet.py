import unittest

from . import increasing_triplet, increasingTriplet


class IncreasingTripletTestCase(unittest.TestCase):
    def test_1_2_3_4_5(self):
        """should return True for [1,2,3,4,5]"""
        nums = [1, 2, 3, 4, 5]
        actual = increasing_triplet(nums)
        self.assertTrue(actual)

    def test_5_4_3_2_1(self):
        """should return false for [5,4,3,2,1]"""
        nums = [5, 4, 3, 2, 1]
        actual = increasing_triplet(nums)
        self.assertFalse(actual)

    def test_2_1_5_0_4_6(self):
        """should return true for [2,1,5,0,4,6]"""
        nums = [2, 1, 5, 0, 4, 6]
        actual = increasing_triplet(nums)
        self.assertTrue(actual)

    def test_20_100_10_12_5_13(self):
        """should return true for [[20,100,10,12,5,13]]"""
        nums = [20, 100, 10, 12, 5, 13]
        actual = increasingTriplet(nums)
        self.assertTrue(actual)


if __name__ == "__main__":
    unittest.main()
