import unittest

from pystrings.latest_time import maximum_time


class LatestTimeTestCases(unittest.TestCase):
    def test_time_missing_second_hour_and_first_minute_ie_2___0(self):
        time = "2?:?0"
        expected = "23:50"
        actual = maximum_time(time)
        self.assertEqual(expected, actual)

    def test_time_missing_second_hour_and_second_minute_0__3_(self):
        time = "0?:3?"
        expected = "09:39"
        actual = maximum_time(time)
        self.assertEqual(expected, actual)

    def test_time_missing_second_hour_only_ie_1__22(self):
        time = "1?:22"
        expected = "19:22"
        actual = maximum_time(time)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
