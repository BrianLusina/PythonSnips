import unittest
import re

"""
check whether the string x or the string o is present, if so, check the count
else, return false
"""


def xoxo(stringer):
    stringer = stringer.lower()
    if stringer.find("x") != -1 and stringer.find("o") != -1:
        return stringer.count("x") == stringer.count("o")
    else:
        return False


def xoxo_reg(stringer):
    X = re.findall(r"(o)+(x)(o)+|(x)+(o)(x)+", stringer, re.IGNORECASE)
    O = re.findall(r"(x)+(o)(x)+", stringer, re.IGNORECASE)
    return len(X) == len(O)


class Tests(unittest.TestCase):
    def test1(self):
        self.assertEqual(True, xoxo("hav fun..xoxo"))

    def test2(self):
        self.assertEqual(False, xoxo("6546516541465"))

    def test3(self):
        self.assertEqual(False, xoxo("xooxxxxooxo"))

    def test4(self):
        self.assertEqual(True, xoxo("xoxoxoxoxoxoxo"))

    def test5(self):
        self.assertEqual(False, xoxo_reg("I have no idea what x is"))
