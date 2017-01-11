from __future__ import division

import math
from operator import mul
from itertools import product
from functools import reduce


class VampireNumbers(object):
    """

    """

    def prime_factors(self, n):
        """
        return the prime factors for n
        # >>> prime_factors(600)
        [5, 5, 3, 2, 2, 2]
        # >>> prime_factors(1000)
        [5, 5, 5, 2, 2, 2]
        """
        step = lambda x: 1 + x * 4 - (x // 2) * 2
        maxq = int(math.floor(math.sqrt(n)))
        d = 1
        q = n % 2 == 0 and 2 or 3
        while q <= maxq and n % q != 0:
            q = step(d)
            d += 1
        res = []
        if q <= maxq:
            res.extend(self.prime_factors(n // q))
            res.extend(self.prime_factors(q))
        else:
            res = [n]
        return res

    def prime_factor_count(self, n):
        """
        How many times the prime factor appears
        :rtype: tuple
        :return the prime factors and their multiplicities for n as a tuple with the 1st elment as the prime factor
        the 2nd element the multiplicity, how many times it appears
        # >>> prime_factor_count(600)
        [(2, 3), (3, 1), (5, 2)]
        # >>> prime_factor_count(1000)
        [(2, 3), (5, 3)]
        """
        res = self.prime_factors(n)
        return [(c, res.count(c)) for c in set(res)]

    def divisors(self, n):
        """
        Returns all the divisors of n
        """

        # Get the prime factor count, store in a list, [(prime_factor, multiplicity), ...]
        factors = self.prime_factor_count(n)

        # unpack the primes and their multiplicities into their own tuples
        # primes = (p, p + 1, p + 2), max_powers = (m, m + 1, m + 2)
        primes, max_powers = zip(*factors)

        # create a generator object for max_powers
        # [range(0, m+1), range(0, m + 2), range(0, m + 3)]
        power_ranges = (range(m + 1) for m in max_powers)

        # get the cartesian product for the power ranges
        powers = product(*power_ranges)
        return (
            reduce(mul, (prime ** power for prime, power in zip(primes, power_group)), 1)
            for power_group in powers)

    def vampire(self, n):
        """

        :param n: number to check if it is a vampire
        :return: fang pairs for number
        """
        fang_sets = set(frozenset([d, n // d])
                        for d in self.divisors(n)
                        if (len(str(d)) == len(str(n)) / 2.
                            and sorted(str(d) + str(n // d)) == sorted(str(n))
                            and (str(d)[-1] == 0) + (str(n // d)[-1] == 0) <= 1))
        return sorted(tuple(sorted(fangs)) for fangs in fang_sets)

    def vampire_test(self, x, y):
        """
        Test whether 2 numbers are vampire numbers
        :param x: 1st number
        :param y: 2nd number
        :return: True /False
        :rtype: bool
        """
        product_ = x * y
        if len(str(x) + str(y)) != len(str(product_)):
            return False

        for i in str(x) + str(y):
            if i in str(x * y):
                return True
            else:
                return False
