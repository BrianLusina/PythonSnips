"""
This finds the sum of all primes below a target limit
"""
from pysnips.math_pysnips.sieve_of_erastothenese import sieve
import cProfile


def find_sum_of_primes(limit):
    """
    Finds the sum of all primes below a target limit. It is always assumed that the starting point in the range will
    be 2, as there is no prime number below 2

    An example:
    >>> find_sum_of_primes(10)
    17

    :param limit: Target limit
    :return: Sum of all primes below the given limit
    :rtype: int
    """

    # find all the primes below the target limit
    all_primes = sieve(limit)

    return sum(all_primes)


if __name__ == "__main__":
    cProfile.run("find_sum_of_primes(2_000_000)")