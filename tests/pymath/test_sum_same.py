import unittest

from pymath.sum_same import sum_same


class SumSameDigTests(unittest.TestCase):
    def test_9(self):
        self.assertEqual(11106, sum_same(9, 4))
