import unittest
from pysnips.strings_words.order_please import order


class Tests(unittest.TestCase):
    def test1(self):
        self.assertEqual(order("is2 Thi1s T4est 3a"), "Thi1s is2 3a T4est")
