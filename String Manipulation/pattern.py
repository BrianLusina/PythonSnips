import unittest


"""
Perform checks on the number, if 0, return an empty string,
if 1, return a string literal of 1,
else,find the range of the numbers and convert each to a string and repeat the string x times will adding to another list
join this list with \n
"""


def pattern(n):
    if n == 0:
        return ""
    elif n == 1:
        return "1"
    else:
        return "\n".join([str(x)*x for x in range(1, n+1)])


class Tests(unittest.TestCase):
    def test1(self):
        self.assertEqual(pattern(1), "1")

    def test2(self):
        self.assertEqual(pattern(2), "1\n22")

    def test3(self):
        self.assertEqual(pattern(5), "1\n22\n333\n4444\n55555")
