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
    h, m = map(int, time_in_mirror.split(':'))
    return '{:02}:{:02}'.format(-(h + (m != 0)) % 12 or 12, -m % 60)
