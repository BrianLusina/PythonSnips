import unittest

from pyregex.autocorrect_prank import auto_correct


class AutoCorrectTests(unittest.TestCase):
    def test_one(self):
        self.assertEqual(auto_correct("u"), "your sister")

    def test_two(self):
        self.assertEqual(auto_correct("you"), "your sister")

    def test_three(self):
        self.assertEqual(auto_correct("Youuuuu"), "your sister")

    @unittest.skip
    def test_four(self):
        self.assertEqual(auto_correct("youtube"), "youtube")

    def test_five(self):
        self.assertEqual(auto_correct("I miss you!"), "I miss your sister!")
