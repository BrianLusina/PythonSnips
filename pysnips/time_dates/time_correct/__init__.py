def time_correct(time_string):
    """
    Perform validation on time string
    Split it into the time components, convert each time component to an integer,
    store time components in variables, hour for hour, minute for minutes and second for seconds
    perform operations on each time component
    if time component is not valid, return None
    """

    result = []
    if time_string is None or len(time_string) < 8:
        return time_string
    elif time_string == "":
        return time_string
    else:
        these_times = time_string.split(":")
        for time_unit in these_times:
            hour, minute, second = these_times[0], these_times[1], these_times[2]
            if isinstance(int(hour), int):
                int(hour) < 24
            else:
                return None
