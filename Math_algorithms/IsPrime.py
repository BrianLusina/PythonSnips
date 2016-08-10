
from math import sqrt
from itertools import count,islice
"""
def is_prime(x):
    if x < 2:
        return False
    for n in range(2, (x-1)):
        if x % n == 0:
            return False
    else:
        return True
"""


class PrimeCheck():
    def __init__(self):
        pass

    @staticmethod
    def is_prime(num):
        return num > 1 and all(num % i for i in islice(count(2), int(sqrt(num)-1)))


class Test(object):
    def __init__(self, n):
        self.n = n

    @staticmethod
    def test_function(actual, expected):
        print("Test for " + str(actual) + " passed " if actual == expected else "Test for " + str(actual) + " failed, expected " + str(expected))


Test.test_function(PrimeCheck.is_prime(0), False)#, '0 is not prime')
Test.test_function(PrimeCheck.is_prime(1), False)#, '1 is not prime')
Test.test_function(PrimeCheck.is_prime(2), True)#, '2 is prime')


def divisors(n):
    return len([1, n]) if PrimeCheck.is_prime(n) else len([x for x in range(1, n+1) if n % x == 0])

Test.test_function(divisors(4), 3)
Test.test_function(divisors(5), 2)
Test.test_function(divisors(12), 6)
Test.test_function(divisors(30), 8)