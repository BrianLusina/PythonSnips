import os
from collections import OrderedDict

from pytime.is_leap import is_leap_year

no_of_days = OrderedDict([("01", 31), ("02", 28), ("03", 31), ("04", 30),
                          ("05", 31), ("06", 30), ("07", 31), ("08", 31),
                          ("09", 30), ("10", 31), ("11", 30), ("12", 31)
                          ])


def day_of_programmer(year):
    if year in range(1700, 1918):
        if year % 4 == 0:
            no_of_days["02"] = 29

    elif year in range(1919, 2701):
        if is_leap_year(year):
            no_of_days["02"] = 29

    elapsed_days = 0
    current_month = "01"

    for month, days in no_of_days.items():
        current_num = elapsed_days
        current_month = month

        elapsed_days += days

        if elapsed_days > 256:
            elapsed_days = current_num
            break

    day = 256 - (elapsed_days if year != 1918 else elapsed_days - 13)
    day = day if day > 0 else 1

    return "{}.{}.{}".format(("0%s" % day if day in range(1, 10) else day), current_month, year)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input())

    result = day_of_programmer(year)

    fptr.write(result + '\n')

    fptr.close()
