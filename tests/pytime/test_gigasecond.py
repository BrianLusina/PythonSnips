import unittest
from datetime import datetime

from pytime.gigasecond import Gigasecond


class GigasecondTest(unittest.TestCase):
    def test_1(self):
        gigasecond = Gigasecond(datetime(2011, 4, 25))
        self.assertEqual(
            datetime(2043, 1, 1, 1, 46, 40),
            gigasecond.add_gigasecond()
        )

    def test_2(self):
        gigasecond = Gigasecond(datetime(1977, 6, 13))
        self.assertEqual(
            datetime(2009, 2, 19, 1, 46, 40),
            gigasecond.add_gigasecond()
        )

    def test_3(self):
        gigasecond = Gigasecond(datetime(1959, 7, 19))
        self.assertEqual(
            datetime(1991, 3, 27, 1, 46, 40),
            gigasecond.add_gigasecond()
        )

    def test_4(self):
        gigasecond = Gigasecond(datetime(2015, 1, 24, 22, 0, 0))
        self.assertEqual(
            datetime(2046, 10, 2, 23, 46, 40),
            gigasecond.add_gigasecond()
        )

    def test_5(self):
        gigasecond = Gigasecond(datetime(2015, 1, 24, 23, 59, 59))
        self.assertEqual(
            datetime(2046, 10, 3, 1, 46, 39),
            gigasecond.add_gigasecond()
        )

    def test_yourself(self):
        # customize this to test your birthday and find your gigasecond date:
        your_birthday = datetime(1970, 1, 1)
        your_gigasecond = datetime(2001, 9, 9, 1, 46, 40)
        gigasecond = Gigasecond(your_birthday)
        self.assertEqual(
            your_gigasecond,
            gigasecond.add_gigasecond()
        )

    def test_6(self):
        giga = Gigasecond(datetime(1988, 5, 15))
        date = giga.add_gigasecond()
        self.assertEqual(["2020-01-22", "Wednesday", str((date - datetime.today()).days) + " days left"],
                         giga.get_date())

    def test_7(self):
        giga = Gigasecond(datetime(2015, 2, 17))
        date = giga.add_gigasecond()
        self.assertEqual(["2046-10-26", "Friday", str((date - datetime.today()).days) + " days left"], giga.get_date())


if __name__ == '__main__':
    unittest.main()
