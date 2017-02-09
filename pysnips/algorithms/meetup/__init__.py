import datetime
from calendar import Calendar

INDEX = {"1st": 0, "2nd": 1, "3rd": 2, "4th": 3, "last": -1}


def meetup_day(year, month, day_of_week, which):
    """
    Gets the meetup date given the year, month day of the week to meet and which day exactly for the meetup
    :param year: Year of meetup
    :param month: month of meetup
    :param day_of_week: day of the week
    :param which: which day of the week, 1st, last, eenth
    :return: datetime object
    """
    # will create an iterator object from Calendar and check for both the month and the day of the week
    candidates = [date for date in Calendar().itermonthdates(year, month)
                  if date.month == month
                  if date.strftime("%A") == day_of_week]
    return _choice(which)(candidates)


def _choice(which):
    """

    :param which:
    :return:
    """
    if which == "teenth":
        return lambda dates: next(d for d in dates if 13 <= d.day <= 19)

    ix = -1 if (which == "last") else (int(which[0]) - 1)
    return lambda dates: dates[ix]


def meetup_day_2(year, month, day_of_wk, eenth):
    dow_dict = {"Monday": [], "Tuesday": [], "Wednesday": [], "Thursday": [], "Friday": [], "Saturday": [],
                "Sunday": []}

    # group the days of the month by the days of week
    date = datetime.date(year, month, 1)
    while date.month == month:
        day_name = date.strftime('%A')
        # add the day to the list
        dow_dict[day_name].append(date.day)
        date += datetime.timedelta(days=1)

    # get the day
    if eenth in INDEX:
        n = INDEX[eenth]
        day = dow_dict[day_of_wk][n]

    if eenth == 'teenth':
        day = [x for x in dow_dict[day_of_wk] if 12 < x < 20][0]

    return datetime.date(year, month, day)
