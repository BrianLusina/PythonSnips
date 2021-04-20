from pymath.xbonacci.fibonacci import fib


def even_fibonacci(a, b, limit):
    """
    Find the all the even numbers in a fibonacci sequence up to the given limit
    :param a Starting point of fibonacci sequence
    :param b second number of the sequence
    :param limit Limit of fibonacci sequence
    :return: list of all the even fibonacci numbers
    :rtype: list
    """
    return list(filter(lambda x: x % 2 == 0, fib(a, b, limit)))


if __name__ == "__main__":
    limit_ = 4_000_000
    print(f"Even fibonacci numbers up to {limit_} {even_fibonacci(0, 1, limit_)}")
    print(f"Sum of even fibonacci numbers up to {limit_} {sum(even_fibonacci(0, 1, limit_))}")
