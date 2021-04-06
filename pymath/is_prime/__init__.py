import re
from itertools import count, islice
from math import sqrt


def is_prime(num):
    return num > 1 and all(num % i for i in islice(count(2), int(sqrt(num) - 1)))


def is_prime_v2(x):
    if x < 2:
        return False
    for n in range(2, (x - 1)):
        if x % n == 0:
            return False
    else:
        return True


def is_prime_with_re(num):
    """
    Determines a prime number with regular expression
    :param num: The number to evaluate for primarity
    :return: True /False
    :rtype: bool
    """
    return re.match(r'^1?$|^(11+?)\1+$', "1" * num) is None


def divisors(n):
    return len([1, n]) if is_prime(n) else len([x for x in range(1, n + 1) if n % x == 0])
