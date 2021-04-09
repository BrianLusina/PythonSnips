import unittest

from pyregex.money_value import money_value


class MoneyValueTestCases(unittest.TestCase):
    def test_money_value_1(self):
        self.assertEqual(money_value("12.34"), 12.34)

    def test_money_value_2(self):
        self.assertEqual(money_value(" $5.67"), 5.67)

    def test_money_value_3(self):
        self.assertEqual(money_value("-0.89"), -0.89)

    def test_money_value_4(self):
        self.assertEqual(money_value("-$ 0.1"), -0.10)

    def test_money_value_5(self):
        self.assertEqual(money_value("$-2.3456"), -2.3456)

    def test_money_value_6(self):
        self.assertEqual(money_value("007"), 7.00)

    def test_money_value_7(self):
        self.assertEqual(money_value(" $ 89"), 89.0)

    def test_money_value_8(self):
        self.assertEqual(money_value("   .11"), 0.11)

    def test_money_value_9(self):
        self.assertEqual(money_value("$.2"), 0.20)

    def test_money_value_10(self):
        self.assertEqual(money_value("-.34"), -0.34)

    def test_money_value_11(self):
        self.assertEqual(money_value("$$$"), 0.0)


if __name__ == '__main__':
    unittest.main()
