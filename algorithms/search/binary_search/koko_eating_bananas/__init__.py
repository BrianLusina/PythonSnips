from typing import List
from math import ceil


def min_eating_speed(piles: List[int], h: int) -> int:
    left, right = 1, 10**9
    result = -1

    while left <= right:
        mid = (left + right) // 2

        if can_finish_eating(piles, h, mid):
            result = mid
            right = mid - 1
        else:
            left = mid + 1

    return result


def can_finish_eating(piles: List[int], h: int, k: int) -> bool:
    hours_used = 0

    for pile in piles:
        # Since Koko eats at only one pile during each hour, ceil(float(p)/k) is the time Koko takes to finish one pile
        # Note that p/k does not work here because we want a whole number of hours so we needed to round up p/k.
        # Therefore, the feasibility is determined by whether Koko's hours_used is within h hours, where hours_used is
        # the total hours to finish all piles.
        hours_used += ceil(float(pile) / k)

    return hours_used <= h
