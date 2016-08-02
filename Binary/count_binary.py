import unittest


def countBits(n):
    return '{0:b}'.format(n).count("1")


class Tests(unittest.TestCase):
    def Test2(self):
        self.assertEqual(countBits(0), 0) 

    def Test3(self):
        self.assertEqual(countBits(4), 1) 

    def Test4(self):
        self.assertEqual(countBits(7), 3) 

    def Test5(self):
        self.assertEqual(countBits(9), 2) 

    def Test6(self):
        self.assertEqual(countBits(10), 2) 