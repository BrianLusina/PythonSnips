import unittest
from Regex.AutocorrectPrank.autocorrect import autocorrect


class AutocorrectTests(unittest.TestCase):
    def test_one(self):
        self.assertEqual(autocorrect("u"), "your sister")

    def test_two(self):
        self.assertEqual(autocorrect("you"), "your sister")

    def test_three(self):
        self.assertEqual(autocorrect("Youuuuu"), "your sister")

    def test_four(self):
        self.assertEqual(autocorrect("youtube"), "youtube")
