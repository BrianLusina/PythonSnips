from datetime import date


def count_sundays_in_20th_century():
    """
    Counts all the sundays in the 20th century i.e. from 1 Jan 1901 to Dec 2000 that fell on the first of the month
    :return: Number of Sundays in 20th Century
    :rtype: int
    """
    counter = 0

    year = 1901
    month = 1

    # set the current date
    current_date = date(year, month, 1)

    # check the first day of each month from 1901 to 2000, check if it is Sunday and increment the counter
    while current_date.year < 2001:

        # current date of the week is Sunday
        if current_date.weekday() == 6:
            counter += 1

        if month + 1 == 13:
            month = 1
            year += 1

        else:
            month += 1
        current_date = date(year, month, 1)

    return counter


if __name__ == "__main__":
    print(f"Number of Sundays in 20th Century that fall on the 1st of the month are {count_sundays_in_20th_century()}")
