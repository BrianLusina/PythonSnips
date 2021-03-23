import re


def seven_ate9(sevens):
    return re.sub(r"7+9(?=7)", "7", sevens)
