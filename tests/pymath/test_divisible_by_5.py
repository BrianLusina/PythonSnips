import unittest

from pymath.binary.divisible_by_5 import Divisible5


class Tests(unittest.TestCase):
    def test1(self):
        que = Divisible5("0100,0011,1010,1001")
        self.assertEqual("1010", que.div_five())

    def test2(self):
        que = Divisible5("0100,0011,1010,1001")
        self.assertEqual("1010", que.div_five_tw0())
