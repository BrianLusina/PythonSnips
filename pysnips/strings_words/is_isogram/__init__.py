import re


def is_isogram(word):
    s = word.lower()
    return len(set(s)) == len(s)
