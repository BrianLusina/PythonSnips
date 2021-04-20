import unittest

from pymath.visible_cubes import VisibleCubes


class VisibleCubesTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(VisibleCubes.not_visible_cubes(0), 0)

    def test_2(self):
        self.assertEqual(VisibleCubes.not_visible_cubes(1), 0)

    def test_3(self):
        self.assertEqual(VisibleCubes.not_visible_cubes(2), 0)

    def test_4(self):
        self.assertEqual(VisibleCubes.not_visible_cubes(3), 1)

    def test_5(self):
        self.assertEqual(VisibleCubes.not_visible_cubes(4), 8)
