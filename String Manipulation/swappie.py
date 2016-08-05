import unittest


class Swap(object):
    def __init__(self, str_input):
        self.str_input = str_input

    def swappie(self):
        out = ""
        for x in self.str_input:
            if x.islower():
               out += x.upper()
            else:
                out += x.lower()
        return out

    def swappie_two(self):
        return self.str_input.swapcase()


class Tests(unittest.TestCase):
    def test1(self):
        word = Swap("Hello World")
        self.assertEqual("hELLO wORLD", word.swappie())

    def test2(self):
        word = Swap("Hello World")
        self.assertEqual("hELLO wORLD", word.swappie_two())
