import unittest
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

num = 20
den = 60

print(Fraction(num % den, den)._numerator)
print(Fraction(num % den, den)._denominator)
print(str(45 // 120) + ' and ' + str(Fraction(num % den, den)) if num//den != 0 else str(Fraction(num % den, den)))


class Test(unittest.TestCase):
    def testOne(self):
        self.assertEqual([3, 1], reduce([60, 20]))

    def testTwo(self):
        self.assertEqual([2, 3], reduce([80, 120]))

    def testThree(self):
        self.assertEqual([2, 1], reduce([4, 2]))

    def testFour(self):
        self.assertEqual([3, 8], reduce([45, 120]))

    def testFive(self):
        self.assertEqual([2, 1], reduce([4, 2]))

    def testSix(self):
        self.assertEqual([2, 1], reduce([4, 2]))

    def testSeven(self):
        self.assertEqual([2, 1], reduce([4, 2]))

    def testEight(self):
        self.assertEqual([1000, 1], reduce([1000, 1]))

    def testNine(self):
        self.assertEqual([1, 1], reduce([1, 1]))