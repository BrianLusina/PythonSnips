from math import sqrt
from itertools import count, islice


def nth_prime(n):
    """
    Returns the nth prime number
    """
    known = []
    candidates = primes()

    def is_prime(num):
        """
        Checks if num is a prime Number
        :param num: number to check for primarity
        :return boolean
        """
        m = sqrt(num)
        for k in known:
            if k > m:
                return True
            elif num % k == 0:
                return False
        return True
    
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