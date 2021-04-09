import unittest

from pystrings.order_please import order


class Tests(unittest.TestCase):
    def test1(self):
        self.assertEqual(order("is2 Thi1s T4est 3a"), "Thi1s is2 3a T4est")

    def test_2_empty_string(self):
        self.assertEqual(order(""), "")

    def test_3(self):
        self.assertEqual(order("is3 my1 brian4 name2"), "my1 name2 is3 brian4")
