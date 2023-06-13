import unittest

from . import product_except_self


class ProductOfArrayExceptSelfTestCases(unittest.TestCase):
    def test_1_2_3_4_returns_24_12_8_6(self):
        """Should return [24,12,8, 6] from input of [1,2,3,4]"""
        nums = [1, 2, 3, 4]
        expected = [24, 12, 8, 6]
        actual = product_except_self(nums)

        self.assertEqual(expected, actual)

    def test_1_1_0_3_3_returns_0_0_9_0_0(self):
        """Should return [0,0,9,0,0] from input of [-1,1,0,-3,3]"""
        nums = [-1, 1, 0, -3, 3]
        expected = [0, 0, 9, 0, 0]
        actual = product_except_self(nums)

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
