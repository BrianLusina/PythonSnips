import unittest

from pystrings.tower_builder import tower_builder


class TowerBuilderTests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(tower_builder(1), ['*', ])

    def test_2(self):
        self.assertEqual(tower_builder(2), [' * ', '***'])

    def test_3(self):
        self.assertEqual(tower_builder(3), ['  *  ', ' *** ', '*****'])
