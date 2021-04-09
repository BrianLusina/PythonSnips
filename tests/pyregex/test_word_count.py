import unittest

from pyregex.word_count import word_count


# todo check on word count
@unittest.skip
class WordCountTests(unittest.TestCase):
    def test1(self):
        self.assertEqual(word_count("hello there"), 2)

    def test2(self):
        self.assertEqual(word_count("hello there and a hi"), 4)

    def test3(self):
        self.assertEqual(word_count("I'd like to say goodbye"), 6)

    def test4(self):
        self.assertEqual(word_count("Slow-moving user6463 has been here"), 6)

    def test5(self):
        self.assertEqual(word_count("%^&abc!@# wer45tre"), 3)

    def test6(self):
        self.assertEqual(word_count("abc123abc123abc"), 3)

    def test7(self):
        self.assertEqual(word_count("Really2374239847 long ^&#$&(*@# sequence"), 3)
