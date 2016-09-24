def is_valid_HK_phone_number(number):
    # check if a space is at the end or at the beginning
    if number.startswith(" ") or number.endswith(" "):
        return False
    # if there are spaces in the middle or none at all
    elif number.count(" ") == 2 or number.count(" ") == 0:
        return False
    # check for validity of numbers
    else:
        nList = number.split()
        if nList[0].isdigit() and len(nList[0]) == 4:
            return True
        elif nList[1].isdigit() and len(nList[1]) == 4:
            return True
        else:
            return False


def has_valid_HK_phone_number(number):
    return filter(lambda x:x.isdigit(),number)