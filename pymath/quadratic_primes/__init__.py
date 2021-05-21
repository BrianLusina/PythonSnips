"""
Given the formula n^2 + an + b, where |a| < 1000 and |b| ≤ 1000
Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes
for consecutive values of n, starting with n=0.
"""
from pymath.primes.is_prime import is_prime


def find_coef_a_b_with_max_primes(n=0):
    """
    Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of
    primes for consecutive values of n, starting with n=0.
    :param n: Starting point, defaults to 0
    :type n int
    :return: product of a and b
    :rtype: int
    """
    num = n
    max_primes = 0
    product = 0

    for a in range(-999, 1001):
        for b in range(-999, 1001):
            while True:
                s = num ** 2 + a * num + b
                if not is_prime(s):
                    break

                if num > max_primes:
                    max_primes = num
                    product = a * b
                num += 1
    return product


if __name__ == "__main__":
    start = 0
    product_a_b = find_coef_a_b_with_max_primes(start)
    print(f"Product of coefficient a and b with maximum primes with starting point n of {start} is {product_a_b}")
