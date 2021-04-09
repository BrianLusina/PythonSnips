import unittest

from pystrings.word_search import word_search


class WordTests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(word_search("ab", ["za", "ab", "abc", "zab", "zbc"]), ["ab", "abc", "zab"])

    def test_2(self):
        self.assertEqual(word_search("aB", ["za", "ab", "abc", "zab", "zbc"]), ["ab", "abc", "zab"])

    def test_3(self):
        self.assertEqual(word_search("ab", ["za", "aB", "Abc", "zAB", "zbc"]), ["aB", "Abc", "zAB"])

    def test_4(self):
        self.assertEqual(word_search("abcd", ["za", "aB", "Abc", "zAB", "zbc"]), ["None"])
