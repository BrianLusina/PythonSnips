from functools import reduce

from pymath.primes.nth_prime import primes_up_to


def multiplier(x, y):
    return x * y


def num_primorial(n):
    known = primes_up_to(n)

    return reduce(multiplier, known)
