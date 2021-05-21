from itertools import count
from typing import List

from ..is_prime import is_prime


def primes_up_to(n: int) -> List[int]:
    """
    Returns a list of prime numbers from 2, up to n
    """
    known = []
    candidates = primes()

    while len(known) < n:
        x = next(candidates)
        if is_prime(x):
            known.append(x)
    return known


def nth_prime(n):
    """
    Returns the nth prime number
    """
    known = primes_up_to(n)
    return known[n - 1]


def primes():
    yield 2
    yield 3
    for x in count(6, 6):
        yield x - 1
        yield x + 1
