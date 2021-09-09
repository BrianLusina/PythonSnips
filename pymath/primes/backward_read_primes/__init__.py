from typing import List, Union

from ..is_prime import is_prime
from ..sieve_of_erastothenese import sieve


def backwards_prime(start: int, stop: int) -> Union[List[int], int]:
    result = []

    # find all primes between start and stop
    primes = sieve(limit=stop, start=start)

    # for each prime, check if the reversed ordering of its digits is a prime
    for prime in primes:
        rev_prime = str(prime)[::-1]
        if is_prime(int(rev_prime)) and not rev_prime == str(prime):
            result.append(prime)

    return result
