from datetime import datetime as dt


def get_time_diff(date1, date2):
    fmt = "%a %d %b %Y %H:%M:%S %z"
    diff = dt.strptime(date1, fmt) - dt.strptime(date2, fmt)
    return int(abs(diff.total_seconds()))
