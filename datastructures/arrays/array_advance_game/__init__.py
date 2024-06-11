from typing import List


def array_advance(a: List[int]) -> bool:
    furthest_reached = 0
    last_idx = len(a) - 1
    i = 0

    while i <= furthest_reached < last_idx:
        furthest_reached = max(furthest_reached, a[i] + i)
        i += 1

    return furthest_reached >= last_idx
