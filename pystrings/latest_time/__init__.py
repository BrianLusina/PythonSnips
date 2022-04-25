import re


def maximum_time(time: str) -> str:
    """
    Takes in a time with a single digit of either the hour part or minute part hidden with ?. The format of the time
    is hh:mm. This returns the maximum possible time from the given input.
    @param time: time of format hh:mm with a single digit of either the hour part or minute part hidden with ?
    @return: Maximum possible time
    """
    hh, mm = time.replace("?", "\\d").split(":")
    hour = re.search(hh, " ".join([str(h).zfill(2) for h in range(23, -1, -1)]))
    minute = re.search(mm, " ".join([str(m).zfill(2) for m in range(59, -1, -1)]))
    return hour[0] + ":" + minute[0]
