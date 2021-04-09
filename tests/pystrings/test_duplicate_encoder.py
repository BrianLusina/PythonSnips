import unittest

from pystrings.duplicate_encoder import DuplicateEncoder


class Tests(unittest.TestCase):
    def test1(self):
        dup = DuplicateEncoder("din")
        self.assertEqual("(((", dup.duplicate_encode())

    def test2(self):
        dup = DuplicateEncoder("recede")
        self.assertEqual("()()()", dup.duplicate_encode())

    def test3(self):
        dup = DuplicateEncoder("Success")
        self.assertEqual(")())())", dup.duplicate_encode(), "should ignore case")

    def test4(self):
        dup = DuplicateEncoder("(( @")
        self.assertEqual("))((", dup.duplicate_encode())
