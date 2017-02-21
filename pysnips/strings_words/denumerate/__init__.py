def denumerate(enum_list):
    """
    denumerates a list of tuples into a word
    :param enum_list: list of tuples with the 1st index in the tuple being the position of the letter (the 2nd elem)
    :return: a word formed from the 'denumeration' or False if it does not start from 0
    :rtype: str or bool
    """
    # resulting string
    string_build = ""

    # sort the list of tuples
    sorted_list = sorted(enum_list)

    # loop through the sorted list, pick the position and add it to the string
    # check if the letter is not alphanumeric, return False immediately
    for pos, let in sorted_list:
        if not let.isalnum():
            return False
        else:
            string_build += let
    return string_build
