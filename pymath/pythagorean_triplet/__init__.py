import cProfile
from functools import reduce
from itertools import islice, count, product
from math import sqrt, pow
from operator import mul


def is_prime(num):
    return num > 1 and all(num % i for i in islice(count(2), int(sqrt(num) - 1)))


PRIMES = [num for num in range(2, 1001) if is_prime(num)]


def factors_powers(num):
    global PRIMES
    if num == 1:
        return (1,), (0,)
    factors, powers, idx = [], [], 0
    while num > 1:
        prime = PRIMES[idx]
        idx += 1
        if num % prime != 0:
            continue
        factors.append(prime)
        p = 0
        while num % prime == 0:
            p += 1
            num /= prime
        powers.append(p)
    return factors, powers


def primitive_triplets(b):
    if b % 4 != 0:
        raise ValueError("Argument must be divisible by 4")
    prime_factors, powers = factors_powers(b / 2)
    args = [(1, pow(prime_factors[x], powers[x])) for x in range(len(powers))]
    a = sorted([reduce(mul, p) for p in product(*args)])
    factors = [(m, n) for m, n in zip(reversed(a), a) if m > n]
    ts = set()
    for m, n in factors:
        l = sorted([b, m * m - n * n, m * m + n * n])
        ts.update([tuple(l)])
    return ts


def is_pythagorean_triplet(abc):
    """
    Checks if a tuple triplet is a pythagorean triplet, i.e. adheres to the rule of a**2 + b**2 = c**2

    An example:

    >>> abc = (29, 20, 21)
    >>> is_pythagorean_triplet(abc)
    True

    >>> abc = (25, 25, 1225)
    >>> is_pythagorean_triplet(abc)
    False

    :param abc: Tuple with the three numbers to check
    :return: True if the tuple meet the given condition
    :rtype: bool
    """
    t = sorted(abc)
    a, b, c = t
    return c * c == a * a + b * b


def triplets_in_range(mini, maxi):
    """
    Finds all the triplets in a given range that meet the condition a ** 2 + b ** 2 = c ** 2

    >>> triplets_in_range(2, 10)
    {(3, 4, 5), (6, 8, 10)}

    :param mini: The minimum in the range
    :param maxi: Maximum in the rnage
    :return: a set of tuples (with length 3) of numbers that meet the given condition
    :rtype: set
    """
    res = set()
    for a in range(mini, maxi + 1):
        for b in range(a + 1, maxi + 1):
            c = int(sqrt(a * a + b * b) + 0.5)
            if c * c == a * a + b * b and mini <= c <= maxi:
                res.update([(a, b, c,)])
    return res


if __name__ == "__main__":
    cProfile.run('is_prime(1000)')
