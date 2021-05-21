from ..is_prime import is_prime


def sieve(limit, start=2):
    """
    Finds all the prime numbers from start (defaults to 2) up to the given limit
    :param limit: Limit to get primes up to
    :param start: Start of the range
    :return: List of all primes from start up to limit
    """
    to_sieve = range(start, limit + 1)
    return list(filter(is_prime, to_sieve))
