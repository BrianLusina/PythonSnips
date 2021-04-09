import unittest

from pystrings.denumerate import denumerate


class Tests(unittest.TestCase):
    def test1(self):
        self.assertEqual(denumerate([(4, 'y'), (1, 'o'), (3, 't'), (0, 'm'), (2, 'n')]), 'monty')

    def test2(self):
        self.assertEqual(denumerate([(1, '3'), (2, 'l'), (4, 'o'), (3, 'l'), (0, 'h')]), 'h3llo')

    def test3(self):
        self.assertEqual(denumerate([(0, '%')]), False)

    def test4(self):
        self.assertEqual(denumerate([(1, 'a'), (2, 'b')]), False)
