"""
Finds the minimum number of coins that sum up to the total change given the total change due and the list of coins with
denominations
"""
from itertools import combinations_with_replacement


def find_minimum_coins(total_change, coins):
    """
    Finds the minimum number coins that add up to the total change given a list of coins. This should return a list of
    the coins that add up to the total change
    :param total_change: Total change due
    :type total_change int
    :param coins: list of denominations
    :type coins list
    :return: list with the least amount of coins that sum up to the total change
    :rtype list
    """
    # return early when there is no change
    if total_change == 0:
        return []

    if total_change < 0:
        raise ValueError("Cannot find change of negative values")

    if total_change < min(coins):
        raise ValueError("Cannot find change if total change is smaller than smallest coin")

    result = None

    for n in range(total_change):
        for combination in combinations_with_replacement(coins, n):
            if sum(combination) == total_change:
                return list(combination)
    if result is None:
        raise ValueError("No combination can add up to target")
