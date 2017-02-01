from itertools import islice, count, product
from math import sqrt, pow
from functools import reduce
from operator import mul
import cProfile


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


def is_triplet(abc):
    t = sorted(list(abc))
    a, b, c = t
    return c * c == a * a + b * b


def triplets_in_range(mini, maxi):
    res = set()
    for a in range(mini, maxi + 1):
        for b in range(a + 1, maxi + 1):
            c = int(sqrt(a * a + b * b) + 0.5)
            if c * c == a * a + b * b and mini <= c <= maxi:
                res.update([(a, b, c,)])
    return res


def main():
    cProfile.run('is_prime(1000)')


if __name__ == "__main__":
    main()
