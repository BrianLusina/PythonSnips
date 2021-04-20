from collections import Counter
from math import sqrt

from pymath.get_next_prime import get_next_prime


def is_triangle_number(number):
    """
    Checks if a number is a triangle number, Returns False fo any input that is not an integer

    An example
    >>> is_triangle_number(8)
    False

    Returns False for none integer inputs
    >>> is_triangle_number(None)
    False

    Returns True for 1
    >>> is_triangle_number(1)
    True

    :param number: Number
    :return: Boolean value, True if number is a triangle number, False otherwise
    :rtype: bool
    """
    if not isinstance(number, int):
        return False
    x = (sqrt(8 * number + 1) - 1) / 2
    if x - int(x) > 0:
        return False
    return True


def find_highly_divisible_triangle_number(no_of_divisors):
    """
    Finds the value of the first triangle number with over a certain number of divisors, in this case the no_of_divisors

    :param no_of_divisors: Number of divisors
    :return: Triangle number with over the given number of divisors
    :rtype: int
    """

    def prime_factorize(num):
        factors = []
        number = abs(num)
        while number > 1:
            factor = get_next_prime(number)
            factors.append(factor)
            number /= factor

        if num < -1:
            factors[0] = -factors[0]
        return factors

    highly_divisible_triangle_num = 1

    while True:
        triangle = highly_divisible_triangle_num * (highly_divisible_triangle_num + 1) / 2
        factors = prime_factorize(triangle)
        counts = Counter(factors)
        divisors = 1
        for k, v in counts.items():
            divisors *= v + 1
        if divisors >= no_of_divisors:
            highly_divisible_triangle_num = triangle
            break
        highly_divisible_triangle_num += 1

    return highly_divisible_triangle_num


if __name__ == "__main__":
    number_of_divisors = 500
    print(f"First triangular number to have over {number_of_divisors} divisors is "
          f"{find_highly_divisible_triangle_number(number_of_divisors)}")
