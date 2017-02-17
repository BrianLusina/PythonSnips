import re


def is_valid_HK_phone_number(number):
    """
    Checks if a number is a valid HK number. will first start checking if there are spaces at either end and return
    false immediately. Will then check if the number contains any spaces within it, if there are 2 or more than 2
     spaces or none at all will return false immediately
    Then proceeds to check for validity of number using a pattern
    :param number: Number to check for validity
    :return: True/False
    :rtype:bool
    """
    # check if a space is at the end or at the beginning
    if number.startswith(" ") or number.endswith(" "):
        return False
    # if there are spaces in the middle or none at all
    elif number.count(" ") == 2 or number.count(" ") == 0:
        return False
    # check for validity of numbers
    else:
        n_list = number.split()
        pattern = "^[0-9]{4}$"
        if re.match(pattern, n_list[0]) and re.match(pattern, n_list[1]):
            return True
        else:
            return False


def has_valid_HK_phone_number(number):
    """
    Checks if a hong kong phone number has a valid phone number
    :param number: the string which may contain a valid hong kong number
    :return: True/False
    :rtype:bool
    """
    match = re.match("([0-9]+)|([0-9]+\s+)|(\s+[0-9]+)|([0-9]+\s[0-9]+)", number)
    print(match)
    if match:
        return is_valid_HK_phone_number(match.group())

print(has_valid_HK_phone_number("Hello, my phone number is 1234 5678"), True)
print(has_valid_HK_phone_number("85748475 is definitely invalid"), False)
