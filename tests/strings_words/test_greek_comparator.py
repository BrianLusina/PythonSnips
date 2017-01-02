import unittest
from pysnips.strings_words.greek_comparator import greek_comparator


class GreekComparator(unittest.TestCase):
    def test_1(self):
        self.assertEqual(greek_comparator('alpha', 'beta'), 0, "result should be negative")

    def test_2(self):
        self.assertEqual(greek_comparator('chi', 'chi'), "")

    def test_3(self):
        self.assertEqual(greek_comparator('upsilon', 'rho'), "")
