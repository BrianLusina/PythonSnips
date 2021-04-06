"""
Finds the smallest multiple in a range of numbers
"""
from functools import reduce

try:
    from math import gcd
except ImportError:
    from fractions import gcd


def smallest_multiple(limit):
    """
    Find the smallest positive number that is evenly divisible by all numbers from 1 to the given
    limit
    :return: smallest positive number
    :rtype: int
    """
    numbers = range(1, limit)
    return reduce(lambda a, b: int(a * b / gcd(a, b)), numbers)


if __name__ == "__main__":
    limit = 21
    result = smallest_multiple(limit)
    print(f"Smallest positive number in range of 1 to {limit} is {result}")
