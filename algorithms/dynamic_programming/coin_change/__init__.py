"""
Finds the minimum number of coins that sum up to the total change given the total change due and the list of coins with
denominations
"""

from typing import List
from itertools import combinations_with_replacement


def find_minimum_coins(total_change: int, coins: List[int]) -> List[int]:
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
        raise ValueError(
            "Cannot find change if total change is smaller than smallest coin"
        )

    result = None

    for n in range(total_change):
        for combination in combinations_with_replacement(coins, n):
            if sum(combination) == total_change:
                return list(combination)
    if result is None:
        raise ValueError("No combination can add up to target")
    return []


def coin_change(coins: List[int], total: int) -> int:
    if total == 0:
        return 0
    # Initialize dimensions: number of coin types and target amount
    num_coins = len(coins)

    # Create 2D DP table
    # dp[i][j] represents minimum coins needed to make amount j using first i coin types
    dp = [[float("inf")] * (total + 1) for _ in range(num_coins + 1)]

    # Base case: 0 coins needed to make amount 0
    dp[0][0] = 0

    # Fill the DP table
    for coin_idx in range(1, num_coins + 1):
        current_coin_value = coins[coin_idx - 1]

        for current_amount in range(total + 1):
            # Option 1: Don't use the current coin type
            dp[coin_idx][current_amount] = dp[coin_idx - 1][current_amount]

            # Option 2: Use the current coin if possible
            if current_amount >= current_coin_value:
                # Compare with using one more of the current coin
                dp[coin_idx][current_amount] = min(
                    dp[coin_idx][current_amount],
                    dp[coin_idx][current_amount - current_coin_value] + 1,
                )

    # Return result: -1 if impossible, otherwise the minimum number of coins
    return -1 if dp[num_coins][total] == float("inf") else dp[num_coins][total]


def coin_change_dp(coins: List[int], total: int) -> int:
    if total < 1:
        return 0
    counter: List[int | float] = [float("inf")] * total

    def calculate_minimum_coins(remaining_amount: int) -> int:
        if remaining_amount < 0:
            return -1
        if remaining_amount == 0:
            return 0
        if counter[remaining_amount - 1] != float("inf"):
            return counter[remaining_amount - 1]

        minimum = float("inf")

        for coin in coins:
            result = calculate_minimum_coins(remaining_amount - coin)
            if 0 <= result < minimum:
                minimum = 1 + result

        counter[remaining_amount - 1] = minimum if minimum != float("inf") else -1
        return counter[remaining_amount - 1]

    return calculate_minimum_coins(remaining_amount=total)
