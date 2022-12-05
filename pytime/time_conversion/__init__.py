def time_conversion(s: str) -> str:
    hh, mm, ss = s.split(":")
    seconds = ss[:2]
    am_or_pm = ss[2:]
    is_pm = "PM" in am_or_pm
    if is_pm:
        hour = f"{int(hh) + 12}" if hh != "12" else hh
    else:
        hour = "00" if hh == "12" else hh

    return f"{hour}:{mm}:{seconds}"
