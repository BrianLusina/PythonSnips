import unittest

from . import max_profit_with_fee


class MaxProfitWithFeeTestCases(unittest.TestCase):
    def test_empty_array(self):
        nums = []
        expected = 0
        actual = max_profit_with_fee(nums, 4)
        self.assertEqual(expected, actual)

    def test_prices_are_same(self):
        nums = [1, 1, 1, 1]
        expected = 0
        actual = max_profit_with_fee(nums, 4)
        self.assertEqual(expected, actual)

    def test_single_element_array(self):
        nums = [1]
        expected = 0
        actual = max_profit_with_fee(nums, 1)
        self.assertEqual(expected, actual)

    def test_4(self):
        """should return 8 for prices=1,3,2,8,4,9 and fee of 2"""
        nums = [1, 3, 2, 8, 4, 9]
        fee = 2
        expected = 8
        actual = max_profit_with_fee(nums, fee)
        self.assertEqual(expected, actual)

    def test_5(self):
        """should return 6 for prices=1,3,7,5,10,3 and fee of 3"""
        nums = [1, 3, 7, 5, 10, 3]
        fee = 3
        expected = 6
        actual = max_profit_with_fee(nums, fee)
        self.assertEqual(expected, actual)

    def test_6(self):
        """should return 13 for prices=[1,4,6,2,8,3,10,14] and fee of 3"""
        nums = [1, 4, 6, 2, 8, 3, 10, 14]
        fee = 3
        expected = 13
        actual = max_profit_with_fee(nums, fee)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
