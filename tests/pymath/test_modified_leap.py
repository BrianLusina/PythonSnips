import unittest

from pymath.modified_leap import year_days


class ModifiedLeapTests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(year_days(0), '0 has 366 days')

    def test_2(self):
        self.assertEqual(year_days(-64), '-64 has 366 days')

    def test_3(self):
        self.assertEqual(year_days(2016), '2016 has 366 days')

    def test_4(self):
        self.assertEqual(year_days(1974), '1974 has 365 days')

    def test_5(self):
        self.assertEqual(year_days(-10), '-10 has 365 days')

    def test_6(self):
        self.assertEqual(year_days(666), '666 has 365 days')

    def test_7(self):
        self.assertEqual(year_days(1857), '1857 has 365 days')

    def test_8(self):
        self.assertEqual(year_days(2000), '2000 has 366 days')

    def test_9(self):
        self.assertEqual(year_days(-300), '-300 has 365 days')

    def test_10(self):
        self.assertEqual(year_days(-1), '-1 has 365 days')
