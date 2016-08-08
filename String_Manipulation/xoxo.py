import unittest

"""
check whether the string x or the string o is present, if so, check the count
else, return false
"""


def xoxo(stringer):
    stringer = stringer.lower()
    if stringer.find("x") != -1 or stringer.find("o") != -1:
        return stringer.count("x") == stringer.count("o")
    return False


class Tests(unittest.TestCase):
    def test1(self):
        self.assertEqual(True, xoxo("hav fun..xoxo"))

    def test2(self):
        self.assertEqual(False, xoxo("6546516541465"))

    def test(self):
        self.assertEqual(False, "xooxxxxooxo")
