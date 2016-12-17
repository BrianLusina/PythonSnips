import datetime


INDEX = {"1st": 0, "2nd": 1, "3rd": 2, "4th": 3, "last": -1}


def meetup_day(year, month, day_of_wk, eenth):
    dow_dict = {"Monday": [], "Tuesday": [], "Wednesday": [], "Thursday": [], "Friday": [], "Saturday": [], "Sunday": []}

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

