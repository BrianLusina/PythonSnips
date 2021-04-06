import calendar
from datetime import timedelta, datetime


class Gigasecond(object):
    def __init__(self, birthday):
        self.birthday = birthday

    def add_gigasecond(self):
        """
        adds 1 billion seconds to someone's birthday, and returns a datetime object with the day someone will turn
        exactly exactly 1 Gs
        :return: datetime object
        """
        return self.birthday + timedelta(seconds=10 ** 9)

    def get_date(self):
        """
        Get the exact date, one will turn exactly 1Gs
        :return: a list with the date, day of the week and how many days left to the date of their birthday
        :rtype: list
        """
        date = self.add_gigasecond()
        return [str(date.date()),
                calendar.day_name[date.weekday()],
                str((date - datetime.today()).days) + " days left"
                ]
