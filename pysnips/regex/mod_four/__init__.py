import re


def mod(test):
    return re.compile('^\[\W?(?:[048]|[0-9]*(?:[02468][048]|[13579][26]))\]$')
