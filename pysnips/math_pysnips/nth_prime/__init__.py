from itertools import count
from pysnips.math_pysnips.is_prime import is_prime


def nth_prime(n):
    """
    Returns the nth prime number
    """
    known = []
    candidates = primes()

    while len(known) < n:
        x = next(candidates)
        if is_prime(x):
            known.append(x)
    return known[n - 1]


def primes():
    yield 2
    yield 3
    for x in count(6, 6):
        yield x - 1
        yield x + 1
