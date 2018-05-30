import unittest

from pysnips.math_pysnips.calc_with_functions import seven, five, divided_by, six, minus,  plus, times, eight, nine, \
    four, one, three, two, zero


class CalcWithFuncs(unittest.TestCase):

    def test_seven_times_five(self):
        self.assertEqual(seven(times(five())), 35)

    def test_four_plus_nine(self):
        self.assertEqual(four(plus(nine())), 13)

    def test_eight_minus_three(self):
        self.assertEqual(eight(minus(three())), 5)

    def test_six_divided_by_two(self):
        self.assertEqual(six(divided_by(two())), 3)


if __name__ == "__main__":
    unittest.main()