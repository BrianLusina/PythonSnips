"""
Checks and matches for a roman numeral
"""
import re


def check_roman_numerals(phrase):
    """
    checks for roman numerals, returns True if roman numeral is valid in a given phrase
    :param phrase: word, sentence or roman numeral
    :return: True if a valid roman numeral is found
    """
    thousand = 'M{0,3}'
    hundred = '(C[MD]|D?C{0,3})'
    ten = '(X[CL]|L?X{0,3})'
    digit = '(I[VX]|V?I{0,3})'
    return bool(re.match(thousand + hundred + ten + digit + '$', phrase))
