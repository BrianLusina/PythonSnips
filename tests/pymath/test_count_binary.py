import unittest

from pymath.binary.count_binary import count_bits


class Tests(unittest.TestCase):
    def Test2(self):
        self.assertEqual(count_bits(0), 0)

    def Test3(self):
        self.assertEqual(count_bits(4), 1)

    def Test4(self):
        self.assertEqual(count_bits(7), 3)

    def Test5(self):
        self.assertEqual(count_bits(9), 2)

    def Test6(self):
        self.assertEqual(count_bits(10), 2)
