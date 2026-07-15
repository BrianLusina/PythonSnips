import unittest

from algorithms.dynamic_programming.buy_sell_stock import (
    max_profit,
    max_profit_two_pointers,
)


class MaxProfitTestCases(unittest.TestCase):
    def test_empty_array(self):
        nums = []
        expected = 0
        actual = max_profit(nums)
        self.assertEqual(expected, actual)

    def test_prices_are_same(self):
        nums = [1, 1, 1, 1]
        expected = 0
        actual = max_profit(nums)
        self.assertEqual(expected, actual)

    def test_single_element_array(self):
        nums = [1]
        expected = 0
        actual = max_profit(nums)
        self.assertEqual(expected, actual)

    def test_prices_7_1_5_3_6_4_should_return_5(self):
        nums = [7, 1, 5, 3, 6, 4]
        expected = 5
        actual = max_profit(nums)
        self.assertEqual(expected, actual)

    def test_prices_7_6_4_3_1_should_return_0(self):
        nums = [7, 6, 4, 3, 1]
        expected = 0
        actual = max_profit(nums)
        self.assertEqual(expected, actual)


class MaxProfitTwoPointersTestCases(unittest.TestCase):
    def test_empty_array(self):
        nums = []
        expected = 0
        actual = max_profit_two_pointers(nums)
        self.assertEqual(expected, actual)

    def test_prices_are_same(self):
        nums = [1, 1, 1, 1]
        expected = 0
        actual = max_profit_two_pointers(nums)
        self.assertEqual(expected, actual)

    def test_single_element_array(self):
        nums = [1]
        expected = 0
        actual = max_profit_two_pointers(nums)
        self.assertEqual(expected, actual)

    def test_prices_7_1_5_3_6_4_should_return_5(self):
        nums = [7, 1, 5, 3, 6, 4]
        expected = 5
        actual = max_profit_two_pointers(nums)
        self.assertEqual(expected, actual)

    def test_prices_7_6_4_3_1_should_return_0(self):
        nums = [7, 6, 4, 3, 1]
        expected = 0
        actual = max_profit_two_pointers(nums)
        self.assertEqual(expected, actual)

    def test_6(self):
        """310, 315, 275, 295, 260, 270, 290, 230, 255, 250 should return 30"""
        nums = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
        expected = 30
        actual = max_profit_two_pointers(nums)
        self.assertEqual(expected, actual)

    def test_7(self):
        """100, 180, 260, 310, 40, 535, 695 should return 655"""
        nums = [100, 180, 260, 310, 40, 535, 695]
        expected = 655
        actual = max_profit_two_pointers(nums)
        self.assertEqual(expected, actual)

    def test_8(self):
        """50, 40, 30, 20, 10 should return 0"""
        nums = [50, 40, 30, 20, 10]
        expected = 0
        actual = max_profit_two_pointers(nums)
        self.assertEqual(expected, actual)

    def test_9(self):
        """110, 215, 180, 335, 5 should return 225"""
        nums = [110, 215, 180, 335, 5]
        expected = 225
        actual = max_profit_two_pointers(nums)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
