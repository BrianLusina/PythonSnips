from datetime import datetime


def unlucky_days(year):
    """
    Calculate the number of Friday 13 in the year
    :param year: The year to calculate number of Friday 13th
    :rtype: int
    """
    return sum(datetime(year, month, 13).weekday() == 4 for month in range(1, 13))
