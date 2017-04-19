import re


def caps_counter(word):
    result = {"UPPER CASE": 0, "LOWER CASE": 0}
    for x in word:
        if re.match(r"[A-Z]", x):
            result["UPPER CASE"] += 1
        elif re.match(r'[a-z]', x):
            result['LOWER CASE'] += 1
    return result
