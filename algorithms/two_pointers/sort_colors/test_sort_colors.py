import unittest
from . import sort_colors, sort_colors_v2


class SortColorsV2TestCase(unittest.TestCase):
    def test_1(self):
        """should sort colors = [1,0,2,1,2,2] to [0,1,1,2,2,2]"""
        colors = [1, 0, 2, 1, 2, 2]
        expected = [0, 1, 1, 2, 2, 2]
        actual = sort_colors_v2(colors)
        self.assertEqual(expected, actual)

    def test_2(self):
        """should sort colors = [0,1,1,2,0,2,0,2,1,2] to [0,0,0,1,1,1,2,2,2,2]"""
        colors = [0, 1, 1, 2, 0, 2, 0, 2, 1, 2]
        expected = [0, 0, 0, 1, 1, 1, 2, 2, 2, 2]
        actual = sort_colors_v2(colors)
        self.assertEqual(expected, actual)

    def test_3(self):
        """should sort colors = [0] to [0]"""
        colors = [0]
        expected = [0]
        actual = sort_colors_v2(colors)
        self.assertEqual(expected, actual)

    def test_4(self):
        """should sort colors = [0,1,0] to [0,0,1]"""
        colors = [0, 1, 0]
        expected = [0, 0, 1]
        actual = sort_colors_v2(colors)
        self.assertEqual(expected, actual)

    def test_5(self):
        """should sort colors = [1] to [1]"""
        colors = [1]
        expected = [1]
        actual = sort_colors_v2(colors)
        self.assertEqual(expected, actual)

    def test_6(self):
        """should sort colors = [2,2] to [2,2]"""
        colors = [2, 2]
        expected = [2, 2]
        actual = sort_colors_v2(colors)
        self.assertEqual(expected, actual)

    def test_7(self):
        """should sort colors = [1,1,0,2] to [0,1,1,2]"""
        colors = [1, 1, 0, 2]
        expected = [0, 1, 1, 2]
        actual = sort_colors_v2(colors)
        self.assertEqual(expected, actual)

    def test_8(self):
        """should sort colors = [2,1,1,0,0] to [0,0,1,1,2]"""
        colors = [2, 1, 1, 0, 0]
        expected = [0, 0, 1, 1, 2]
        actual = sort_colors_v2(colors)
        self.assertEqual(expected, actual)


class SortColorsTestCase(unittest.TestCase):
    def test_1(self):
        """should sort colors = [1,0,2,1,2,2] to [0,1,1,2,2,2]"""
        colors = [1, 0, 2, 1, 2, 2]
        expected = [0, 1, 1, 2, 2, 2]
        actual = sort_colors(colors)
        self.assertEqual(expected, actual)

    def test_2(self):
        """should sort colors = [0,1,1,2,0,2,0,2,1,2] to [0,0,0,1,1,1,2,2,2,2]"""
        colors = [0, 1, 1, 2, 0, 2, 0, 2, 1, 2]
        expected = [0, 0, 0, 1, 1, 1, 2, 2, 2, 2]
        actual = sort_colors(colors)
        self.assertEqual(expected, actual)

    def test_3(self):
        """should sort colors = [0] to [0]"""
        colors = [0]
        expected = [0]
        actual = sort_colors(colors)
        self.assertEqual(expected, actual)

    def test_4(self):
        """should sort colors = [0,1,0] to [0,0,1]"""
        colors = [0, 1, 0]
        expected = [0, 0, 1]
        actual = sort_colors(colors)
        self.assertEqual(expected, actual)

    def test_5(self):
        """should sort colors = [1] to [1]"""
        colors = [1]
        expected = [1]
        actual = sort_colors(colors)
        self.assertEqual(expected, actual)

    def test_6(self):
        """should sort colors = [2,2] to [2,2]"""
        colors = [2, 2]
        expected = [2, 2]
        actual = sort_colors(colors)
        self.assertEqual(expected, actual)

    def test_7(self):
        """should sort colors = [1,1,0,2] to [0,1,1,2]"""
        colors = [1, 1, 0, 2]
        expected = [0, 1, 1, 2]
        actual = sort_colors(colors)
        self.assertEqual(expected, actual)

    def test_8(self):
        """should sort colors = [2,1,1,0,0] to [0,0,1,1,2]"""
        colors = [2, 1, 1, 0, 0]
        expected = [0, 0, 1, 1, 2]
        actual = sort_colors(colors)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
