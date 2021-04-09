"""
Replaces && and || in a string to 'and' and 'or'
"""
import re

N = int(input())


def replace(match_obj):
    return "and" if match_obj.group(0) == "&&" else "or"


for _ in range(N):
    print(re.sub(r"(?<= )(&&|[|]{2})(?= )", replace, input()))
