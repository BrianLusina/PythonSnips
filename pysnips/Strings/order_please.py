import unittest
import re

"""
Split the string into a list,
Loop through it checking if the number in the string is greater than the number in the next string
if the current string has a number that is less than the next, add it to a result string
        re.match(r'\w+([0-9]*)\w+|\w+([0-9]*)|([0-9]*)\w+', sentence)

"""


def order(sentence):
    sent_li = sentence.split(" ")
    indx, res = 0, ""
    while indx < len(sent_li):
        for x in sent_li:
            for i in x[indx]:
                if i.isdigit():
                    pass
        indx += 1
    return res


class Tests(unittest.TestCase):
    def test1(self):
        self.assertEqual(order("is2 Thi1s T4est 3a"), "Thi1s is2 3a T4est")
