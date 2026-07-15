import math
from typing import List


def minimize(a: List[int], b: List[int], c: List[int]) -> int:
    """minimizes the maximum difference
    Windowing strategy works here.
    Take 3 pointers i, j and k

    Initialize them to point to the start of arrays a, b and c
    Find min of i, j and k.
    Compute max(i, j, k) - min(i, j, k).
    If the new result is less than the current result, change it to the new result.
    Increment the pointer of the array which contains the minimum.

    Note that we increment the pointer of the array which has the minimum, because our goal is to decrease the difference.
    Increasing the maximum pointer is definitely going to increase the difference. Increasing the second maximum pointer
    can potentially increase the difference (however, it certainly will not decrease the difference).
    """
    current_min = math.inf
    i, j, k = 0, 0, 0

    while i < len(a) and j < len(b) and k < len(c):
        a_num = a[i]
        b_num = b[j]
        c_num = c[k]

        current = max(abs(a_num - b_num), abs(b_num - c_num), abs(c_num - a_num))
        current_min = min(current_min, current)

        # get the minimum of the three numbers, for the number that matches this minimum; their pointer is moved. The intent
        # is to minimize the difference
        min_of_3 = min(a_num, b_num, c_num)

        if a_num == min_of_3:
            i += 1
        elif b_num == min_of_3:
            j += 1
        else:
            k += 1

    return current_min
