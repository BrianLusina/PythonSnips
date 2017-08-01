from itertools import islice, count
from math import sqrt


def sieve(limit):
    to_sieve = range(2, limit + 1)
    return list(filter(lambda x: x > 1 and all(x % i for i in islice(count(2), int(sqrt(x)-1))), to_sieve))
