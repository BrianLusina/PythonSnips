import unittest

from pymath.power_digit_sum import power_digit_sum


class PowerDigitSumTestCase(unittest.TestCase):

    def test_2_to_power_15(self):
        self.assertEqual(power_digit_sum(2, 15), 26)

    def test_2_to_power_1000(self):
        self.assertEqual(power_digit_sum(2, 1000), 1366)


if __name__ == '__main__':
    unittest.main()
