def time_correct(time_string):
    """
    Perform validation on time string
    Split it into the time components, convert each time component to an integer,
    store time components in variables, hour for hour, minute for minutes and second for seconds
    perform operations on each time component
    if time component is not valid, return None
    """

    if time_string is None:
        return time_string
    if time_string == "":
        return time_string
    if len(time_string) < 8:
        return None
    else:
        try:
            # get the hour, minute and second from the time string
            hour, minute, second = map(int, time_string.split(":"))
        except ValueError:
            return None

        if second >= 60:
            # if the second is greater than 60 add 1 minute
            minute += second // 60
            second %= 60

        # if the minute is greater than 60, add 1 hour and re-set the minutes to the remainder
        if minute >= 60:
            hour += minute // 60
            minute %= 60

        if hour >= 24:
            hour %= 24

        return "%02d:%02d:%02d" % (hour, minute, second)
