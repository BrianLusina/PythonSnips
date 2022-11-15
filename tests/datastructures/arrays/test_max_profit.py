import unittest

from datastructures.arrays.max_profit import max_profit, max_profit_two_pointers, max_profit_2


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


class MaxProfit2TestCases(unittest.TestCase):
    def test_empty_array(self):
        nums = []
        expected = 0
        actual = max_profit_2(nums)
        self.assertEqual(expected, actual)

    def test_prices_are_same(self):
        nums = [1, 1, 1, 1]
        expected = 0
        actual = max_profit_2(nums)
        self.assertEqual(expected, actual)

    def test_single_element_array(self):
        nums = [1]
        expected = 0
        actual = max_profit_2(nums)
        self.assertEqual(expected, actual)

    def test_prices_7_1_5_3_6_4_should_return_7(self):
        nums = [7, 1, 5, 3, 6, 4]
        expected = 7
        actual = max_profit_2(nums)
        self.assertEqual(expected, actual)

    def test_prices_7_6_4_3_1_should_return_0(self):
        nums = [7, 6, 4, 3, 1]
        expected = 0
        actual = max_profit_2(nums)
        self.assertEqual(expected, actual)

    def test_prices_1_2_3_4_5_should_return_4(self):
        nums = [1, 2, 3, 4, 5]
        expected = 4
        actual = max_profit_2(nums)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
