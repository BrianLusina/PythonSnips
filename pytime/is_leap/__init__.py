"""
Checks if a year is leap
From  1700 to 1917, Russia's official calendar was the Julian calendar; since  they used the Gregorian calendar system.
The transition from the Julian to Gregorian calendar system occurred in , when the next day after January  was February.
 This means that in , February  was the  day of the year in Russia.

In both calendar systems, February is the only month with a variable amount of days; it has  days during a leap year,
and days during all other years. In the Julian calendar, leap years are divisible by ; in the Gregorian calendar,
leap years are either of the following:

Divisible by 400.
Divisible by 4 and not divisible by 100.

"""


def is_leap_year(year):
    """
    Checks if a year is a leap year
    :param year: Year
    :type year int
    :return:
    :rtype: bool
    """
    return True if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0 else False
