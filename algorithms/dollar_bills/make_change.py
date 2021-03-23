from itertools import combinations, combinations_with_replacement

dollar_bills = [20, 20, 20, 10, 10, 10, 10, 10, 5, 5, 1, 1, 1, 1, 1]


def make_change_for_100(bills):
    """
    Finds the number of ways we can make change for a 100 dollar bill, given the
    list of the dollar bills
    An example:
    >>> bill_list = [20, 20, 20, 10, 10, 10, 10, 10, 5, 5, 1, 1, 1, 1, 1]
    >>> make_change_for_100(bill_list)
    5

    :return: Number of ways of making change for a 100 dollar bill
    :rtype: int
    """
    result = []

    for n in range(1, len(bills) + 1):
        for combination in combinations(bills, n):
            if sum(combination) == 100:
                result.append(combination)

    return len(set(result))


def make_change_for_100_with_any():
    """
    Finds the number of possible combinations of $50, $20, $10, $5, and $1 bills that sum up to $100
    An examples:
    >>> make_change_for_100_with_any()
    343

    :return: Number of all possible combinations to sum up to 100
    :rtype: int
    """
    bills = [50, 20, 10, 5, 1]
    makes_100 = []

    for n in range(1, 101):
        for combination in combinations_with_replacement(bills, n):
            if sum(combination) == 100:
                makes_100.append(combination)

    return len(makes_100)
