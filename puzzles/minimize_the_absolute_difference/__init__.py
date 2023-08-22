from typing import List


def minimize_absolute_difference(a: List[int], b: List[int], c: List[int]) -> int:
    i = len(a) - 1
    j = len(b) - 1
    k = len(c) - 1

    min_diff = abs(max(a[i], b[j], c[k]) - min(a[i], b[j], c[k]))

    while i != -1 and j != -1 and k != -1:
        current_diff = abs(max(a[i], b[j], c[k]) - min(a[i], b[j], c[k]))

        # checking condition
        if current_diff < min_diff:
            min_diff = current_diff

        # calculating max term from list
        max_term = max(a[i], b[j], c[k])

        # Moving to smaller value in the
        # array with maximum out of three.
        if a[i] == max_term:
            i -= 1
        elif b[j] == max_term:
            j -= 1
        else:
            k -= 1
    return min_diff
