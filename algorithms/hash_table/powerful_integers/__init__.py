from typing import List, Set
from math import log


def powerful_integers(x: int, y: int, bound: int) -> List[int]:
    # Use a set to store unique powerful integers
    result_set: Set[int] = set()

    # Compute powers of x up to bound
    # If x == 1, x^i is always 1, so only need i=0
    pow_x = 1  # x^0 = 1
    while pow_x <= bound:
        # For each power of x, iterate over powers of y
        pow_y = 1  # y^0 = 1
        while pow_x + pow_y <= bound:
            # Add the powerful integer to the set
            result_set.add(pow_x + pow_y)
            # If y is 1, y^j is always 1, so break after first iteration
            if y == 1:
                break
            # Move to next power of y
            pow_y *= y
        # If x is 1, x^i is always 1, so break after first iteration
        if x == 1:
            break
        # Move to next power of x
        pow_x *= x

    # Convert set to list and return
    return list(result_set)


def powerful_integers_logarithmic_bounds(x: int, y: int, bound: int) -> List[int]:
    if bound == 0:
        return []

    a = bound if x == 1 else int(log(bound, x))
    b = bound if y == 1 else int(log(bound, y))

    result_set = set([])

    for i in range(a + 1):
        for j in range(b + 1):
            value = x**i + y**j

            if value <= bound:
                result_set.add(value)

            if y == 1:
                break

        if x == 1:
            break

    return list(result_set)
