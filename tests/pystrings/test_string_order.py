import unittest

from pystrings.string_order import order


class StringOrderTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(order("is2 Thi1s T4est 3a"), "Thi1s is2 3a T4est")

    def test_2(self):
        self.assertEqual(order('Fo1r the2 g3ood th5e 4of pe6ople'), 'Fo1r the2 g3ood 4of th5e pe6ople')
