import re


def maskify(cc):
    return cc if len(cc) <= 4 else re.sub(r'.', r'#', cc[:-4]) + cc[len(cc) - 4:]
