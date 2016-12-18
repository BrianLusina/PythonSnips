import unittest
from strings_words.is_isogram import is_isogram


class Tests(unittest.TestCase):
    """
    Tests the isogram function
    """

    def test1(self):
        self.assertEqual(is_isogram("Dermatoglyphics"), True)

    def test2(self):
        self.assertEqual(is_isogram("isogram"), True)

    def test3(self):
        self.assertEqual(is_isogram("aba"), False, "same chars may not be adjacent")

    def test4(self):
        self.assertEqual(is_isogram("moOse"), False, "same chars may not be same case")

    def test5(self):
        self.assertEqual(is_isogram("isIsogram"), False)

    def test6(self):
        self.assertEqual(is_isogram(""), True, "an empty string is a valid isogram")
