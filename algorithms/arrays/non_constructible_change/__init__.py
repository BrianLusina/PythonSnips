from typing import List


def non_constructible_change(coins: List[int]) -> int:
    """
    Return the smallest amount of change that cannot be created from the given coins.
    Greedy approach: track the maximum constructible change 'current_change_created'.
    If the next coin is greater than current_change_created + 1, we've found the gap.

    Examples:
    >>> non_constructible_change([5, 7, 1, 1, 2, 3, 22])
    20
    >>> non_constructible_change([])
    1
    >>> non_constructible_change([1, 1, 1, 1, 1])
    6
    """
    # Do not mutate the caller's input; iterate over a sorted copy.
    sorted_coins = sorted(coins)

    current_change_created = 0

    for coin in sorted_coins:
        if coin > current_change_created + 1:
            return current_change_created + 1
        current_change_created += coin

    return current_change_created + 1
