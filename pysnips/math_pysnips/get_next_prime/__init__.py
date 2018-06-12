"""
Gets the next prime number
"""

from math import sqrt


def get_next_prime(n):
    """
    Gets the next prime number from the given prime number
    :param n: Number
    :return: Next prime number in series
    :rtype: int
    """
    if n % 2 == 0:
        return 2
    for x in range(3, int(sqrt(n) + 1), 2):
        if n % x == 0:
            return x
    return n
