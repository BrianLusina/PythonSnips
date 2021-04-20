import unittest

from pymath.expanded_form import expanded_form, expanded_form_2


class ExpandedFormTests(unittest.TestCase):

    def test_12(self):
        self.assertEqual("10 + 2", expanded_form(12))

    def test_42(self):
        self.assertEqual('40 + 2', expanded_form(42))

    def test_70304(self):
        self.assertEqual('70000 + 300 + 4', expanded_form(70304))

    def test_12_expanded_2(self):
        self.assertEqual("10 + 2", expanded_form_2(12))

    def test_42_expanded_2(self):
        self.assertEqual('40 + 2', expanded_form_2(42))

    def test_70304_expanded_2(self):
        self.assertEqual('70000 + 300 + 4', expanded_form_2(70304))
