# -*- coding: utf-8 -*-
import unittest

from pymath.convert_improper_fraction import convert_to_mixed_numeral


class ConvertTests(unittest.TestCase):
    def testOne(self):
        self.assertEqual('3', convert_to_mixed_numeral('6/2'))

    def testTwo(self):
        self.assertEqual('24 2/3', convert_to_mixed_numeral('74/3'))

    def testThree(self):
        self.assertEqual('-19 10/26', convert_to_mixed_numeral('-504/26'))

    def testFour(self):
        self.assertEqual('9/18', convert_to_mixed_numeral('9/18'))

    def testFive(self):
        self.assertEqual('-8', convert_to_mixed_numeral('-64/8'))


if __name__ == '__main__':
    unittest.main()
