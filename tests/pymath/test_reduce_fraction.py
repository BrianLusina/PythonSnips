import unittest

from pymath.reduce_fraction import reduce


class ReduceFractionTestss(unittest.TestCase):
    def testOne(self):
        self.assertEqual([3, 1], reduce([60, 20]))

    def testTwo(self):
        self.assertEqual([2, 3], reduce([80, 120]))

    def testThree(self):
        self.assertEqual([2, 1], reduce([4, 2]))

    def testFour(self):
        self.assertEqual([3, 8], reduce([45, 120]))

    def testFive(self):
        self.assertEqual([2, 1], reduce([4, 2]))

    def testSix(self):
        self.assertEqual([2, 1], reduce([4, 2]))

    def testSeven(self):
        self.assertEqual([2, 1], reduce([4, 2]))

    def testEight(self):
        self.assertEqual([1000, 1], reduce([1000, 1]))

    def testNine(self):
        self.assertEqual([1, 1], reduce([1, 1]))
