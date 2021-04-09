import unittest

from pytime.friday_13th import unlucky_days


class UnluckyDaysTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(unlucky_days(2015), 3, "should be: 3")

    def test_2(self):
        self.assertEqual(unlucky_days(1986), 1, "should be: 1")
