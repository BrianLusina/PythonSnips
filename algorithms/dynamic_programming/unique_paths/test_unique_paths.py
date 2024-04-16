import unittest
from . import unique_paths_top_down, unique_paths_math, unique_paths_bottom_up


class UniquePathsTopDownTestCase(unittest.TestCase):
    def test_1(self):
        """should return 28 for m=3 and n=7"""
        m = 3
        n = 7
        expected = 28
        actual = unique_paths_top_down(m, n)
        self.assertEqual(expected, actual)

    def test_2(self):
        """should return 3 for m=3 and n=2"""
        m = 3
        n = 2
        expected = 3
        actual = unique_paths_top_down(m, n)
        self.assertEqual(expected, actual)


class UniquePathsBottomUpTestCase(unittest.TestCase):
    def test_1(self):
        """should return 28 for m=3 and n=7"""
        m = 3
        n = 7
        expected = 28
        actual = unique_paths_bottom_up(m, n)
        self.assertEqual(expected, actual)

    def test_2(self):
        """should return 3 for m=3 and n=2"""
        m = 3
        n = 2
        expected = 3
        actual = unique_paths_bottom_up(m, n)
        self.assertEqual(expected, actual)


class UniquePathsMathTestCase(unittest.TestCase):
    def test_1(self):
        """should return 28 for m=3 and n=7"""
        m = 3
        n = 7
        expected = 28
        actual = unique_paths_math(m, n)
        self.assertEqual(expected, actual)

    def test_2(self):
        """should return 3 for m=3 and n=2"""
        m = 3
        n = 2
        expected = 3
        actual = unique_paths_math(m, n)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
