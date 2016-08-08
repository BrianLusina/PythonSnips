from datetime import timedelta, datetime
import unittest
import calendar


class Gigasecond(object):
    def __init__(self, birthday):
        self.birthday = birthday

    def add_gigasecond(self):
        return self.birthday + timedelta(seconds=10 ** 9)

    def get_date(self):
        date = self.add_gigasecond()
        return [str(date.date()), calendar.day_name[date.weekday()], str((date - datetime.today()).days) + " days left"]


class Tests(unittest.TestCase):
    def test_1(self):
        giga = Gigasecond(datetime(2011, 4, 25))
        self.assertEqual(datetime(2043, 1, 1, 1, 46, 40), giga.add_gigasecond())

    def test_2(self):
        giga = Gigasecond(datetime(1977, 6, 13))
        self.assertEqual(datetime(2009, 2, 19, 1, 46, 40), giga.add_gigasecond())

    def test_3(self):
        giga = Gigasecond(datetime(1959, 7, 19))
        self.assertEqual(
            datetime(1991, 3, 27, 1, 46, 40), giga.add_gigasecond())

    def test_4(self):
        giga = Gigasecond(datetime(2015, 1, 24, 22, 0, 0))
        self.assertEqual(datetime(2046, 10, 2, 23, 46, 40), giga.add_gigasecond())

    def test_5(self):
        giga = Gigasecond(datetime(2015, 1, 24, 23, 59, 59))
        self.assertEqual(datetime(2046, 10, 3, 1, 46, 39), giga.add_gigasecond())

    def test_yourself(self):
        # customize this to test your birthday and find your gigasecond date:
        your_birthday = datetime(1970, 1, 1)
        giga  = Gigasecond(your_birthday)
        your_gigasecond = datetime(2001, 9, 9, 1, 46, 40)

        self.assertEqual(
            your_gigasecond, giga.add_gigasecond())

    def test_6(self):
        giga = Gigasecond(datetime(1988, 5, 15))
        self.assertEqual(["2020-01-22", "Wednesday", "1764 days left"], giga.get_date())

    def test_7(self):
        giga = Gigasecond(datetime(2015, 2, 17))
        self.assertEqual(["2046-10-26", "Friday", "11538 days left"], giga.get_date())