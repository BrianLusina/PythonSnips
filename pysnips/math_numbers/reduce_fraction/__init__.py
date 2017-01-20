from fractions import Fraction


def reduce(fraction):
    num, den = fraction[0], fraction[1]
    if num == den:
        return [1, 1]
    if num > den:
        num, den = fraction[1], fraction[0]
        return [Fraction(num % den, den).denominator, Fraction(num % den, den).numerator]
    else:
        return [Fraction(num % den, den).numerator, Fraction(num % den, den).denominator]
