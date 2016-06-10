"""
Define a function isPrime that takes one integer argument and returns true or false depending on if the integer is a prime.

Per Wikipedia, a prime number (or a prime) is a natural number greater than 1 that has no positive divisors other than 1 and itself.

Example

isPrime(5)
=> true
Assumptions
You can assume you will be given an integer input.
You can not assume that the integer will be only positive. You may be given negative numbers.
"""
from math import sqrt
from itertools import count,islice

class PrimeCheck():
    def __init__(self):
        pass

    @staticmethod
    def is_prime(num):
        return num > 1 and all(num%i for i in islice(count(2),int(sqrt(num)-1)))


class Test(object):
    def __init__(self, n):
        self.n = n

    @staticmethod
    def test_function(actual, expected):
        print "Test for " + str(actual) + " passed " if actual == expected else "Test for " + str(actual) + " failed, expected " + str(expected)


Test.test_function(PrimeCheck.is_prime(0), False)#, '0 is not prime')
Test.test_function(PrimeCheck.is_prime(1), False)#, '1 is not prime')
Test.test_function(PrimeCheck.is_prime(2), True)#, '2 is prime')