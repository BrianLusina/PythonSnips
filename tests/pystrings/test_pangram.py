# -*- coding: utf-8 -*-

import unittest

from pystrings.pangram import Pangram


class PangramTests(unittest.TestCase):

    def test_empty_string(self):
        pangram = Pangram("")
        self.assertFalse(pangram.is_pangram())

    def test_valid_pangram(self):
        pangram = Pangram('the quick brown fox jumps over the lazy dog')
        self.assertTrue(
            pangram.is_pangram())

    def test_invalid_pangram(self):
        pangram = Pangram('the quick brown fish jumps over the lazy dog')
        self.assertFalse(pangram.is_pangram())

    def test_missing_x(self):
        pangram = Pangram('a quick movement of the enemy will jeopardize five gunboats')
        self.assertFalse(pangram.is_pangram())

    def test_mixedcase_and_punctuation(self):
        pangram = Pangram('"Five quacking Zephyrs jolt my wax bed."')
        self.assertTrue(pangram.is_pangram())

    def test_unchecked_german_umlaute(self):
        pangram = Pangram('Victor jagt zwölf Boxkämpfer quer über den großen Sylter Deich.')
        self.assertTrue(pangram.is_pangram())


if __name__ == '__main__':
    unittest.main()
