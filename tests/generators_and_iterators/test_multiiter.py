import unittest

from generators_and_iterators.iterators.multiiter import multiiter


# todo: fix generator
@unittest.skip
class MultiIterTests(unittest.TestCase):
    def test1(self):
        self.assertEquals(multiiter(0), [])

    def test2(self):
        self.assertEquals(multiiter(2), (0,), (1,))

    def test3(self):
        self.assertEquals(multiiter(2, 3), [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), ])

    def test4(self):
        self.assertEquals(multiiter(3, 2), [(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1), ])
