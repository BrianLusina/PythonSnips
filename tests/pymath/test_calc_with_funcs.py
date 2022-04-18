import unittest

from pymath.calc_with_functions import (
    divided_by,
    eight,
    five,
    four,
    minus,
    nine,
    plus,
    seven,
    six,
    three,
    times,
    two,
)


class CalcWithFuncs(unittest.TestCase):
    @unittest.skip
    def test_seven_times_five(self):
        self.assertEqual(seven(times(five())), 35)

    @unittest.skip
    def test_four_plus_nine(self):
        self.assertEqual(four(plus(nine())), 13)

    @unittest.skip
    def test_eight_minus_three(self):
        self.assertEqual(eight(minus(three())), 5)

    @unittest.skip
    def test_six_divided_by_two(self):
        self.assertEqual(six(divided_by(two())), 3)


if __name__ == "__main__":
    unittest.main()
