from fractions import Fraction
from decimal import Decimal

"""
[[1, 2], [1, 3], [1, 4]]), [13, 12] -> 1/2 + 1/3 + 1/4 = 1.0833
13/12 = 1.0833

"""


def sum_fracts(lst):
    total, n = 0, 0
    if lst is None or len(lst) == 0:
        return None
    for fract in lst:
        total += Fraction(fract[0], fract[1])
    denom = total._denominator
    numer = total._numerator
    if denom is 1:
        return numer
    else:
        return [numer, denom]

print(sum_fracts([[1, 2], [1, 3], [1, 4]]), [13, 12])
print(sum_fracts([[1, 3], [5, 3]]), 2)