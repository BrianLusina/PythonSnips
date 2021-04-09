import unittest

from pystrings.greek_comparator import greek_comparator


class GreekComparator(unittest.TestCase):
    def test_1(self):
        self.assertEqual(greek_comparator('alpha', 'beta'), -1, "result should be negative")

    def test_2(self):
        self.assertEqual(greek_comparator('chi', 'chi'), 0)

    def test_3(self):
        self.assertEqual(greek_comparator('upsilon', 'rho'), 3)
