import unittest


class PowerSumDigTermTests(unittest.TestCase):
    def test_1(self):
        self.assertEquals(power_sumDigTerm(1), 81)

    def test_2(self):
        self.assertEquals(power_sumDigTerm(2), 512)

    def test_3(self):
        self.assertEquals(power_sumDigTerm(3), 2401)

    def test_4(self):
        self.assertEquals(power_sumDigTerm(4), 4913)

    def test_5(self):
        self.assertEquals(power_sumDigTerm(5), 5832)

if __name__ == '__main__':
    unittest.main()
