from datetime import datetime
import unittest

from pysnips.time_dates.gigasecond import add_gigasecond, Gigasecond


class GigasecondTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(
            datetime(2043, 1, 1, 1, 46, 40),
            add_gigasecond(datetime(2011, 4, 25))
        )

    def test_2(self):
        self.assertEqual(
            datetime(2009, 2, 19, 1, 46, 40),
            add_gigasecond(datetime(1977, 6, 13))
        )

    def test_3(self):
        self.assertEqual(
            datetime(1991, 3, 27, 1, 46, 40),
            add_gigasecond(datetime(1959, 7, 19))
        )

    def test_4(self):
        self.assertEqual(
            datetime(2046, 10, 2, 23, 46, 40),
            add_gigasecond(datetime(2015, 1, 24, 22, 0, 0))
        )

    def test_5(self):
        self.assertEqual(
            datetime(2046, 10, 3, 1, 46, 39),
            add_gigasecond(datetime(2015, 1, 24, 23, 59, 59))
        )

    def test_yourself(self):
        # customize this to test your birthday and find your gigasecond date:
        your_birthday = datetime(1970, 1, 1)
        your_gigasecond = datetime(2001, 9, 9, 1, 46, 40)

        self.assertEqual(
            your_gigasecond,
            add_gigasecond(your_birthday)
        )

    def test_6(self):
        giga = Gigasecond(datetime(1988, 5, 15))
        self.assertEqual(["2020-01-22", "Wednesday", "1764 days left"], giga.get_date())

    def test_7(self):
        giga = Gigasecond(datetime(2015, 2, 17))
        self.assertEqual(["2046-10-26", "Friday", "11538 days left"], giga.get_date())


if __name__ == '__main__':
    unittest.main()
