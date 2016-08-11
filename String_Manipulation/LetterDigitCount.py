import unittest


class LetterDigitCount(object):
    def __init__(self, sentence):
        self.sentence = sentence

    def counter(self):
        d = {"DIGITS": 0, "LETTERS": 0}
        for x in self.sentence:
            if x.isdigit():
                d["DIGITS"] += 1
            elif x.isalpha():
                d["LETTERS"] += 1
            else:
                pass

        return d


class Tests(unittest.TestCase):
    def test(self):
        let = LetterDigitCount("hello world! 123")
        self.assertEqual({"LETTERS": 10, "DIGITS": 3}, let.counter())
