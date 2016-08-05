import unittest


class Swap(object):
    def __init__(self, str_input):
        self.str_input = str_input

    # simple solution
    def swappie(self):
        out = ""
        for x in self.str_input:
            if x.islower():
               out += x.upper()
            else:
                out += x.lower()
        return out

    # alternative solution
    def swappie_two(self):
        return self.str_input.swapcase()


class Tests(unittest.TestCase):
    def test1(self):
        word = Swap("Hello World")
        self.assertEqual("hELLO wORLD", word.swappie())

    def test2(self):
        word = Swap("Hello World")
        self.assertEqual("hELLO wORLD", word.swappie_two())

    def test3(self):
        word = Swap("My name Is Brian")
        self.assertEqual("mY NAME iS bRIAN", word.swappie())

    def test4(self):
        word = Swap("help ME")
        self.assertEqual("HELP me", word.swappie())

    def test5(self):
        word = Swap("lorem IPSON")
        self.assertEqual("LOREM ipson", word.swappie())

    def test6(self):
        word = Swap("meme")
        self.assertEqual("MEME", word.swappie())

