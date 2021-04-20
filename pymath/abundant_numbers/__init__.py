from operator import itemgetter

from pymath.perfect_numbers import divisor_generator


def is_deficient(n):
    """
    Checks if a number is deficient, i.e. has sum of divisors that is less than n
    Example:

    >>> is_deficient(35)
    True

    :param n: Number to check for deficiency
    :type n int
    :return: True if the sum is less than the number, False otherwise
    :rtype: bool
    """

    return sum_of_divisors(n) < n


def is_abundant(n):
    """
    Checks if a number is abundant, i.e. has sum of divisors that exceed n
    Example:

    >>> is_abundant(12)
    True

    :param n: Number to check for abundancy
    :type n int
    :return: True if the sum exceeds the number, False otherwise
    :rtype: bool
    """
    return sum_of_divisors(n) > n


def sum_of_divisors(n):
    return sum(divisor_generator(n)) + 1


def abundance_of_num(n):
    return sum_of_divisors(n) - n


def abundance(n):
    if n == 0:
        return []

    abundant_numbers = []
    start_number = 12

    while len(abundant_numbers) < n:
        if is_abundant(start_number):
            abundant_numbers.append((start_number, abundance_of_num(start_number)))
        start_number += 1

    return list(map(itemgetter(0), sorted(abundant_numbers, key=lambda x: x[1])))
