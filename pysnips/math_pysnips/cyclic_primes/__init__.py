from ..is_prime import is_prime
from ..sieve_of_erastothenese import sieve
from itertools import permutations


def find_number_of_cyclic_primes(start, limit):
    """
    Find the number of cyclic primes within the range or 0 to the given limit
    :param limit: Limit to find cyclic primes to
    :param start: the range to start from
    :return: Integer with the number of primes within the given range
    """
    all_primes = sieve(limit, start)
    cyclic_primes = []

    for prime in all_primes:
        if is_prime_cyclic(prime):
            cyclic_primes.append(prime)

    return len(cyclic_primes)


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
        rotations = permutations(str(prime))

        for rot in rotations:
            number = int("".join(rot))
            if not is_prime(number):
                return False
        return True
