import unittest
from pysnips.math_pysnips.expanded_form import expanded_form


class ExpandedFormTests(unittest.TestCase):

    def test_12(self):
        self.assertEqual("10 + 2", expanded_form(12))

    def test_42(self):
        self.assertEqual('40 + 2', expanded_form(42))

    def test_70304(self):
        self.assertEqual('70000 + 300 + 4', expanded_form(70304))