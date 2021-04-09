import unittest
from datetime import date

from pytime.days_till_christmas import days_until_christmas


class DaysTillXmasTestCases(unittest.TestCase):
    def test_1(self):
        self.assertEqual(days_until_christmas(date(2016, 12, 9)), 16)

    def test_2(self):
        self.assertEqual(days_until_christmas(date(2016, 12, 8)), 17)

    def test_3(self):
        self.assertEqual(days_until_christmas(date(1996, 12, 7)), 18)

    def test_4(self):
        self.assertEqual(days_until_christmas(date(2015, 2, 23)), 305)

    def test_5(self):
        self.assertEqual(days_until_christmas(date(2001, 7, 11)), 167)

    def test_6(self):
        self.assertEqual(days_until_christmas(date(2000, 12, 9)), 16)

    def test_7(self):
        self.assertEqual(days_until_christmas(date(1978, 3, 18)), 282)

    def test_8(self):
        self.assertEqual(days_until_christmas(date(2016, 12, 25)), 0)

    def test_9(self):
        self.assertEqual(days_until_christmas(date(2016, 12, 26)), 364)

    def test_10(self):
        self.assertEqual(days_until_christmas(date(2015, 12, 26)), 365)


if __name__ == '__main__':
    unittest.main()
