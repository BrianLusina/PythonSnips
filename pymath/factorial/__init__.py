from functools import wraps
from math import factorial as math_factorial, sqrt, pi, e


def memoize(func):
    cache = func.cache = {}

    @wraps(func)
    def wrapper(n):
        if n not in cache:
            cache[n] = func(n)
        return cache[n]

    return wrapper


def memodict(f):
    """ Memoization decorator for a function taking a single argument """

    class memodict(dict):
        def __missing__(self, key):
            ret = self[key] = f(key)
            return ret

    return memodict().__getitem__


def stirling_approximation(num):
    """
    Uses Stirling approximation to find the factorial of a number. Will NOT return the exact factorial, but an
    approximation of it
    :param num: Number to get factorial of
    :type num int
    :return: Factorial approximation of num
    :rtype: float
    """
    return sqrt(2 * pi * num) * ((num / e) ** num)


# @memoize
def factorial(num):
    """
    find the factorial of the given number
    :param num: Number
    :return: Factorial of num
    :rtype: int
    """
    cache = {}

    if num in cache:
        return cache[num]

    if num == 0:
        return 1

    else:
        x = num * factorial(num - 1)
        cache[num] = x
        return x
    # return 1 if num == 0 else num * factorial(num - 1)


def factorial_digit_sum(num):
    """
    Finds the sum of the digits in the factorial of num

    An example:
    >>> factorial_digit_sum(10)
    27

    :param num: Number
    :type num int
    :return: sum of digits in the factorial of num
    :rtype: int
    """

    # sanity checks
    if num is None or not isinstance(num, (int, float)):
        raise ValueError(f"Expected number to be a number, instead got {num}")

    # convert to integer, in the case of floats
    num = int(num)

    # find the factorial of the number
    num_factorial = factorial(num)

    return sum(map(int, str(num_factorial)))


def factorial_length(num):
    """
    Finds the length of the factorial of number num

    >>> factorial_length(5)
    3

    :param num:
    :type num int
    :return: Length of factorial i.e. number of digits in factorial
    :rtype: int
    """
    n_factorial = math_factorial(num)

    return len(str(n_factorial))
