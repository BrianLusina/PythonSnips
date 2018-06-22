from pysnips.math_pysnips.perfect_numbers import divisor_generator


def is_deficient(n):
    """
    Checks if a number is deficient, i.e. has sum of divisors that is less than n
    Example:

    >>> is_deficient(35)
    True

    :param n: Number to check for deficiency
    :type n int
    :return: True if the sum is less than the number, False otherwise
    :rtype: bool
    """

    return sum(divisor_generator(n)) + 1 < n


def is_abundant(n):
    """
    Checks if a number is abundant, i.e. has sum of divisors that exceed n
    Example:

    >>> is_abundant(12)
    True

    :param n: Number to check for abundancy
    :type n int
    :return: True if the sum exceeds the number, False otherwise
    :rtype: bool
    """
    return sum(divisor_generator(n)) + 1 > n


def find_sum_cant_be_written(lower_limit, upper_limit):
    """
    Finds the sum of all positive integers within the given range, which can not be written as the sum of 2 abundant
    numbers,
    :param lower_limit: Lower limit bound
    :type lower_limit int
    :param upper_limit: upper limit bound
    :type upper_limit int
    :return: sum of all positive integers within range, which can't be written as sum of 2 abundant numbers
    :rtype: int
    """
    # sanity checks

    if lower_limit is None or upper_limit is None:
        raise ValueError("Expected non-None types for bounds lower and upper limit")

    if not isinstance(lower_limit, (int, float)) or not isinstance(upper_limit, (int, float)):
        raise TypeError("Expected number type for upper and lower limits")

    if lower_limit < 0:
        raise ValueError(f"Expected lower limit to be positive, instead got {lower_limit}")

    if upper_limit > 28123:
        raise ValueError(f"Expected upper limit to be less than 28123, instead got {upper_limit}")

    # convert the upper and lower limits to integers, this is for float type inputs
    lower_limit, upper_limit = int(lower_limit), int(upper_limit)

    # find all abundant numbers within the given range
    abundant_numbers = set(x for x in range(lower_limit, upper_limit) if is_abundant(x))

    # list that stores all numbers that can't be written as the sum of 2 abundant numbers
    cant_be_written = []

    for x in range(lower_limit, upper_limit + 1):
        if not any((x - number) in abundant_numbers for number in abundant_numbers):
            cant_be_written.append(x)

    # return the sum of numbers
    return sum(cant_be_written)
