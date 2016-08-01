import unittest
import re

"""
	/*
	([a-zA-Z]) - A letter which it captures in the first group; then
	.*? - zero or more characters (the ? denotes as few as possible); until
	\1 - it finds a repeat of the first matched character.
	*/
	var regex = /([a-zA-Z]).*?\1/gi;
	return !regex.test(this.word);

"""


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
