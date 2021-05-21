"""
Finds the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
"""
from pymath.primes.sieve_of_erastothenese import sieve


def longest_recurring_cycle(limit=1000):
    """
    Finds the longest recurring cycle for a fraction
    An example:
    >>> longest_recurring_cycle(10)
    7

    >>> longest_recurring_cycle(7)
    3

    :param limit: The limit of the denominator, if None is provided, the limit will default to 1000
    :type limit int
    :return: Returns the value of d for which the longest recurring cycle exists in the decimal fraction part
    :rtype: int
    """
    # sanity checks, because we don't want unexpected crashes
    if not isinstance(limit, int) or limit <= 1:
        raise ValueError("Expected limit to be greater than 1 and an integer")

    # we return 3 because that is the smallest d that repeats with the longest recurring cycle. 1/2 (0.5), 1/4 (0.25),
    # 1/5 (0.2) don’t repeat. 1/3 (0.33~), 1/6 (0.166~) both repeat with a cycle of 1 of which 3
    # is the smallest value of d. 3 is not a reptend prime.
    if limit < 8:
        return 3

    prime_sieve = sieve(limit)

    for denominator in prime_sieve[::-1]:
        period = 1
        while pow(10, period) % denominator != 1:
            period += 1
        if denominator - 1 == period:
            return denominator


if __name__ == "__main__":
    limit_ = 1000
    digit_with_recurring_cycle = longest_recurring_cycle(limit_)
    print(f"Digit with longest recurring cycle in its decimal fraction part within range of 2 to {limit_} "
          f"is {digit_with_recurring_cycle}")
