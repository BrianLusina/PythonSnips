min_on_right, min_on_left = range(1, 30), range(31, 60)
hours_on_right, hours_on_left = range(1, 6), range(7, 12)

min_reflections = list(zip(min_on_right, sorted(min_on_left, reverse=True)))
hour_reflections = list(zip(hours_on_right, sorted(hours_on_left, reverse=True)))


def what_is_the_time(time_in_mirror):
    """
    Minutes mirror each other using the middle of the clock as a mirror
    so 25 minutes is mirrored by 35 minutes on the other side
    The middle points are minute 0 and minute 30, which will always be the same no matter what reflection
    is used. Same applies to the hours

    Create ranges for the minutes and the hours
    create reflections for the minutes and the hours
    :param time_in_mirror: time as shown in the mirror
    :return: real time in mirror as a string
    """
    hour, mins = time_in_mirror.split(":")
    h, m = int(hour), int(mins)
    real_min, real_hour = 0, 0

    if h == 12 and m == 0:
        real_hour = 12
    elif h == 6 and m == 0:
        real_hour = 6
    elif h == 12 and m != 0:
        real_hour = 11
    elif h == 6 and m != 0:
        real_hour = 5

    for hours in hour_reflections:
        if h in hours:
            if h == hours[1]:
                real_hour = hours[0]
            else:
                real_hour = hours[1]

    for minutes in min_reflections:
        if m in minutes:
            if m == minutes[1]:
                real_min = minutes[0]
            else:
                real_min = minutes[1]

    return "{:02}:{:02}".format(real_hour, real_min)

print(what_is_the_time("06:02"))
