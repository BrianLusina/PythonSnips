from fractions import Fraction


def sum_fracts(lst):
    total, n = 0, 0
    if lst is None or len(lst) == 0:
        return None
    for fract in lst:
        total += Fraction(fract[0], fract[1])
    denom = total.denominator
    numer = total.numerator
    if denom is 1:
        return numer
    else:
        return [numer, denom]


def sum_fracts_2(lst):
    if lst:
        ret = sum(Fraction(a, b) for (a, b) in lst)
        return ret.numerator if ret.denominator == 1 else [ret.numerator, ret.denominator]