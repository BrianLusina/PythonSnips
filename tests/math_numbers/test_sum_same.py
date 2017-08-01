import unittest
from math_numbers.sum_same import sum_same


class SumSameDigTests(unittest.TestCase):
    def test_9(self):
        self.assertEqual(11106, sum_same(9, 4))
