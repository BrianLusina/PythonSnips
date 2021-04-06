from itertools import count, islice
from math import sqrt


class Pernicious(object):
    """
    get the range of the number from 3 to the number, converting each to binary
    for
    """

    def __init__(self, number):
        self.number = number

    # long method
    def is_pernicious(self):
        primes = []
        if self.number <= 2:
            return "No pernicious numbers"
        for x in range(3, int(self.number) + 1):
            if Pernicious.is_prime(sum([int(i) for i in '{0:b}'.format(x)])):
                primes.append(x)
        return primes

    # using ternary and lambda
    def is_pernicious_v2(self):
        m = lambda i: '{0:b}'.format(i)
        if self.number <= 1:
            return "No pernicious numbers"
        return [x for x in range(3, int(self.number) + 1) if Pernicious.is_prime(sum([int(y) for y in m(x)]))]

    def is_pernicious_v3(self):
        return [x for x in range(int(self.number) + 1) if
                bin(x).count("1") in [2, 3, 5, 7, 11, 13]] or "No pernicious numbers"

    @staticmethod
    def is_prime(num):
        return num > 1 and all(num % i for i in islice(count(2), int(sqrt(num) - 1)))
