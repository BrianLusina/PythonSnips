import unittest

"""
PSEUDO CODE:

"""


def multiiter(*args):
    print(args)
    for x, y in args:
        for a in range(x):
            for b in range(y):
                yield (a, b)


class Tests(unittest.TestCase):
    def test1(self):
        self.assertEquals(list(multiiter(0)), [])

    def test2(self):
        self.assertEquals(list(multiiter(2)), [(0,), (1,)])

    def test3(self):
        self.assertEquals(list(multiiter(2, 3)), [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), ])

    def test4(self):
        self.assertEquals(list(multiiter(3, 2)), [(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1), ])