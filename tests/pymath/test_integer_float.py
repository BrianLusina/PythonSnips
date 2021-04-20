import unittest

from pymath.integer_of_float import i_or_f


class IntegerFloatTests(unittest.TestCase):
    def test_1(self):
        self.assertEquals(i_or_f('1'), True)

    def test_2(self):
        self.assertEquals(i_or_f('1.0'), True)

    def test_3(self):
        self.assertEquals(i_or_f('1e1'), True)

    def test_4(self):
        self.assertEquals(i_or_f('1E-1'), True)

    def test_5(self):
        self.assertEquals(i_or_f('1e+1'), True)
