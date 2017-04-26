import unittest
from pysnips.py_strings_words.letter_digit_count import LetterDigitCount


class Tests(unittest.TestCase):
    def test(self):
        let = LetterDigitCount("hello world! 123")
        self.assertEqual({"LETTERS": 10, "DIGITS": 3}, let.counter())
