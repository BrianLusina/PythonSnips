import unittest

from Scrabble import scrabble


class WordTest(unittest.TestCase):
    def test_invalid_word_scores_zero(self):
        self.assertEqual(0, scrabble.score(''))
        self.assertEqual(0, scrabble.core(' \t\n'))
        self.assertEqual(0, scrabble.score('hous3'))
        self.assertEqual(0, scrabble.score('wo rd'))

    def test_scores_very_short_word(self):
        self.assertEqual(1, scrabble.score('a'))

    def test_scores_other_very_short_word(self):
        self.assertEqual(4, scrabble.score('f'))

    def test_simple_word_the_number_of_letters(self):
        self.assertEqual(6, scrabble.score("street"))

    def test_complicated_word_scores_more(self):
        self.assertEqual(22, scrabble.score("quirky"))

    def test_scores_are_case_insensitive(self):
        self.assertEqual(41, scrabble.score("OxyphenButazone"))

if __name__ == '__main__':
    unittest.main()
