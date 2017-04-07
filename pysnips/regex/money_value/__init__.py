import re


def money_value(s):
    s = s.strip()
    m = re.search(r"([0-9]+\.[0-9]+|-[0-9]+\.[0-9]+|-\$\s[0-9]+\.[0-9]+)", s)