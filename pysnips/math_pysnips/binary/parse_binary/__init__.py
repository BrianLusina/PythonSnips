def parse_binary(num_str):
    """
    Check if all elements of ths string are digits, raise ValueError if not
    loop through the reversed string, converting each to an integer and multiplying it to base 2
    :param num_str: The string to check against
    :raises: ValueError
    :return: The number to base 10
    :rtype: int
    """
    if set(num_str) - set("01"):
        raise ValueError("Invalid binary")
    return sum(int(digit) * 2 ** i for (i, digit) in enumerate(reversed(num_str)))
