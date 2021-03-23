"""
Finds the prime factors of a given number and returns a list of the numbers
"""


def prime_factors(number):
    """
    Finds the prime factors of a number
    :param number: Integer number to find prime factors for
    :return: list of primes factors for the given number
    :rtype: list

    An example
    >>> prime_factors(13195)
    [5, 7, 13, 29]
    """
    c, res = 2, []
    while c * c <= number:
        while (number % c) == 0:
            # repeats multiple factors
            res.append(c)
            number /= c
        c += 1
    if number > 1:
        res.append(number)
    return res
