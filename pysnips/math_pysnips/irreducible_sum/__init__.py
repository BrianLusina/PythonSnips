from fractions import Fraction


def sum_fracts(lst):
    """
    checks if the list is None of has no elements, returns None if so
    loops through each element in the list adding the fraction to the initialized total variable
    accumuletes this variable to the end of the list
    Perform checks for the denominator and numerator, returning either the whole number or the irreducible fraction
    :param lst: list of list with numerator and denominator
    :return: the irreducible form of the rational numbers
    """
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
