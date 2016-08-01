import unittest
import re

"""
([a-zA-Z]) - A letter which it captures in the first group; then
.*? - zero or more characters (the ? denotes as few as possible); until
\1 - it finds a repeat of the first matched character.

Alternatives
Loop through each character in word and check the count of each letter, if the letter is greater than 1, it is not an isogram,
else it is
    w = word.lower()
    for chr in w:
        if w.count(chr) > 1:
            return False
    return True

OR

Use a set to determine if the length of unique characters are equal to the characters already present, if they are then it is an isogram, else it is false
"""


def is_isogram(word):
    s = word.lower()
    return len(set(s)) == len(s)


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
