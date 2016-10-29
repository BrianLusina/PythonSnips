import unittest
from Regex.AutocorrectPrank.autocorrect import auto_correct


class AutocorrectTests(unittest.TestCase):
    def test_one(self):
        self.assertEqual( "your sister", auto_correct("u"))

    def test_two(self):
        self.assertEqual( "your sister", auto_correct("you"))

    def test_three(self):
        self.assertEqual("your sister", auto_correct("Youuuuu"))

    def test_four(self):
        self.assertEqual("youtube", auto_correct("youtube"))

    def test_five(self):
        self.assertEqual("I miss your sister!", auto_correct("I miss you!"))
