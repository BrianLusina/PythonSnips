from functools import reduce


def power_digit_sum(base, exponent):
    """
    Finds the sum of digits of the exponentiation of base to exponent
    Example:

    >>> power_digit_sum(2, 15)
    26

    :param base: Base
    :param exponent: Exponent
    :return: sum of digits of the exponent
    :rtype: int
    """
    result = pow(base, exponent)
    return reduce(lambda x, y: x + y, map(int, [i for i in str(result)]))
