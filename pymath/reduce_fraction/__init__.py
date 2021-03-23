from fractions import Fraction


def reduce(fraction):
    num, den = fraction[0], fraction[1]
    if num == den:
        return [1, 1]
    if num > den:
        num, den = fraction[1], fraction[0]
        return [Fraction(num % den, den)._denominator, Fraction(num % den, den)._numerator]
    else:
        return [Fraction(num % den, den)._numerator, Fraction(num % den, den)._denominator]
