from pymath.primes.is_prime import is_prime
from pymath.primes.sieve_of_erastothenese import sieve


def find_cyclic_primes(start, limit):
    """
    Finds all cyclic primes in a given range
    :param start: Start of range
    :param limit: Limit to find the cyclic primes
    :return: List of all cyclic primes
    :rtype: list
    """
    all_primes = sieve(limit, start)
    cyclic_primes = []

    for prime in all_primes:
        if is_prime_cyclic(prime):
            cyclic_primes.append(prime)

    return cyclic_primes


def find_number_of_cyclic_primes(start, limit):
    """
    Find the number of cyclic primes within the range or 0 to the given limit
    :param limit: Limit to find cyclic primes to
    :param start: the range to start from
    :return: Integer with the number of primes within the given range
    """
    return len(find_cyclic_primes(start, limit))


def find_sum_of_cyclic_primes(start, limit):
    """
    Finds the number of cyclic primes in a given range
    :param start: Where start is the start of the range
    :param limit: Limit is the end of the range
    :return: sum of cyclic primes in a given range
    :rtype: int
    """
    return sum(find_cyclic_primes(start, limit))


def is_prime_cyclic(prime):
    """
    Checks if a prime number is cyclic
    :param prime: Prime number
    :return: Boolean value True if cyclic, False otherwise
    """
    if not prime:
        return False
    else:
        # rotate the prime number
        number_str = str(prime)
        rotations = len(number_str) - 1

        for _ in range(rotations):
            number_str = number_str[-1] + number_str[:-1]
            if not is_prime(int(number_str)):
                return False
        return True


def rotate(num):
    n = str(num)
    return n[1:] + n[:1]
