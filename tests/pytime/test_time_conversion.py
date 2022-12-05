import unittest

from pytime.time_conversion import time_conversion


class TimeConversionTestCases(unittest.TestCase):
    def test_12_01_00_PM_returns_12_01_00(self):
        """Should return 12:01:00 from 12:01:00PM"""
        s = "12:01:00PM"
        expected = "12:01:00"
        actual = time_conversion(s)

        self.assertEqual(expected, actual)

    def test_07_05_45_PM_returns_19_05_45(self):
        """Should return 19:05:45 from 07:05:45PM"""
        s = "07:05:45PM"
        expected = "19:05:45"
        actual = time_conversion(s)

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
