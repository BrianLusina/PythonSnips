import unittest


class RemoveDupSort(object):
    def __init__(self, sentence):
        self.sentence = sentence

    def remover(self):
        words = self.sentence.split(" ")
        return " ".join(sorted(set(words)))


class Tests(unittest.TestCase):
    def test1(self):
        sent = RemoveDupSort("hello world and practice makes perfect and hello world again")
        self.assertEqual("again and hello makes perfect practice world", sent.remover())

