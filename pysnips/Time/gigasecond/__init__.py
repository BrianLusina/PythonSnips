from datetime import timedelta, datetime
import calendar


class Gigasecond(object):
    def __init__(self, birthday):
        self.birthday = birthday

    def add_gigasecond(self):
        return self.birthday + timedelta(seconds=10 ** 9)

    def get_date(self):
        date = self.add_gigasecond()
        return [str(date.date()), calendar.day_name[date.weekday()], str((date - datetime.today()).days) + " days left"]


def add_gigasecond(birthday):
    return birthday + timedelta(seconds=10**9)
