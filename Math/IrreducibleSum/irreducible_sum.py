from fractions import Fraction
from decimal import Decimal

"""
[[1, 2], [1, 3], [1, 4]]), [13, 12] -> 1/2 + 1/3 + 1/4 = 1.0833
13/12 = 1.0833

"""


def sum_fracts(lst):
    if lst is None or len(lst) == 0:
        return None
    for fract in lst:
        pass
    return None


print(sum_fracts([[1, 2], [1, 3], [1, 4]]), [13, 12])
