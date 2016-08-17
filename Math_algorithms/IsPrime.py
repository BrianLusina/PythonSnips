from math import sqrt
import unittest
from itertools import count, islice


class PrimeCheck(object):
    def __init__(self):
        pass

    @staticmethod
    def is_prime(num):
        return num > 1 and all(num % i for i in islice(count(2), int(sqrt(num)-1)))

    @staticmethod
    def is_prime_v2(x):
        if x < 2:
            return False
        for n in range(2, (x-1)):
            if x % n == 0:
                return False
        else:
            return True


class PrimeTests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(PrimeCheck.is_prime(0), False, "0 is not prime")

    def test_2(self):
        self.assertEqual(PrimeCheck.is_prime(1), False, "1 is not prime")

    def test_3(self):
        self.assertEqual(PrimeCheck.is_prime(2), True, "2 is prime")


def divisors(n):
    return len([1, n]) if PrimeCheck.is_prime(n) else len([x for x in range(1, n+1) if n % x == 0])


class DivisorTests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(divisors(4), 3)

    def test_2(self):
        self.assertEqual(divisors(5), 2)

    def test_3(self):
        self.assertEqual(divisors(12), 6)

    def test_4(self):
        self.assertEqual(divisors(30), 8)
