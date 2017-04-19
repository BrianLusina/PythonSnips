import re


def is_valid_HK_phone_number(number):
    """
    Checks if a number is a valid HK number
    Then proceeds to check for validity of number using a pattern
    :param number: Number to check for validity
    :return: True/False
    :rtype:bool
    """
    return bool(re.match("^\d{4} \d{4}$", number))


def has_valid_HK_phone_number(number):
    """
    Checks if a string has a valid phone number
    :param number: the string which may contain a valid hong kong number
    :return: True/False
    :rtype:bool
    """
    return bool(re.search("[0-9]{4} [0-9]{4}", number))
