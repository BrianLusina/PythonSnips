import unittest


class DuplicateEncoder(object):
    def __init__(self, encode):
        self.encode = encode
        
    def duplicate_encode(self):
        encode = self.encode.lower()
        out = ""
        for x in encode:
            if encode.count(x) == 1:
                out += "("
            else:
                out += ")"
        return out


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
