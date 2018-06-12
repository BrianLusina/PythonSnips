from math import sqrt


def is_triangle_number(number):
    """
    Checks if a number is a triangle number, Returns False fo any input that is not an integer

    An example
    >>> is_triangle_number(8)
    False

    Returns False for none integer inputs
    >>> is_triangle_number(None)
    False

    Returns True for 1
    >>> is_triangle_number(1)
    True

    :param number: Number
    :return: Boolean value, True if number is a triangle number, False otherwise
    :rtype: bool
    """
    if not isinstance(number, int):
        return False
    x = (sqrt(8 * number + 1) - 1) / 2
    if x - int(x) > 0:
        return False
    return True
