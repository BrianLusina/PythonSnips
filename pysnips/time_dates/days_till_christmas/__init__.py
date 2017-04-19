from datetime import date


def days_until_christmas(current_date):
    """
    calculates the number of days until christmas given the day object, which will be the current date
    :param current_date: datetime object with the current date
    :return: days until christmas
    :rtype: int
    """
    # extract year from date
    year = current_date.year

    # set the christmas day for the current year
    christmas_day = date(year, 12, 25)

    # if the date is greater than christmas day
    if current_date > christmas_day:
        christmas = date(year + 1, 12, 25)
        return (christmas - current_date).days
    return (christmas_day - current_date).days
