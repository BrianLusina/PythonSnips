import unittest

from pymath.power_of_sum import power_sum_dig_term


class PowerSumDigTermTests(unittest.TestCase):
    def test_1(self):
        self.assertEquals(power_sum_dig_term(1), 81)

    def test_2(self):
        self.assertEquals(power_sum_dig_term(2), 512)

    def test_3(self):
        self.assertEquals(power_sum_dig_term(3), 2401)

    def test_4(self):
        self.assertEquals(power_sum_dig_term(4), 4913)

    def test_5(self):
        self.assertEquals(power_sum_dig_term(5), 5832)


if __name__ == '__main__':
    unittest.main()
