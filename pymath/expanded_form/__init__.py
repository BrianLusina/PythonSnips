def expanded_form(num):
    """
    Expands the form of a number placing all digits in the number into their place values
    :param num: Integer
    :return String representation of the number broken down into its place values
    :rtype: str
    """
    str_num = str(num)
    length = len(str_num)
    result = []

    for digit in str_num:
        if digit != "0":
            result.append(str(int(digit) * int("1{}".format("0" * (length - 1)))))
        length -= 1

    return " + ".join(result)


def expanded_form_2(num):
    """Second implementation of expanded form"""
    result = []
    for a in range(len(str(num)) - 1, -1, -1):
        current = 10 ** a
        quo, num = divmod(num, current)

        if quo:
            result.append(str(quo * current))

    return " + ".join(result)
