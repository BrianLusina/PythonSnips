import unittest

from . import min_flips, min_flips_2


class MinFlipsTestCase(unittest.TestCase):
    def test_1(self):
        """should return 3 from a = 2, b = 6, c = 5"""
        a = 2
        b = 6
        c = 5
        expected = 3
        actual = min_flips(a, b, c)
        self.assertEqual(expected, actual)

    def test_2(self):
        """should return 1 from a = 4, b = 2, c = 7"""
        a = 4
        b = 2
        c = 7
        expected = 1
        actual = min_flips(a, b, c)
        self.assertEqual(expected, actual)

    def test_3(self):
        """should return 0 from a = 1, b = 2, c = 3"""
        a = 1
        b = 2
        c = 3
        expected = 0
        actual = min_flips(a, b, c)
        self.assertEqual(expected, actual)


class MinFlips2TestCase(unittest.TestCase):
    def test_1(self):
        """should return 3 from a = 2, b = 6, c = 5"""
        a = 2
        b = 6
        c = 5
        expected = 3
        actual = min_flips_2(a, b, c)
        self.assertEqual(expected, actual)

    def test_2(self):
        """should return 1 from a = 4, b = 2, c = 7"""
        a = 4
        b = 2
        c = 7
        expected = 1
        actual = min_flips_2(a, b, c)
        self.assertEqual(expected, actual)

    def test_3(self):
        """should return 0 from a = 1, b = 2, c = 3"""
        a = 1
        b = 2
        c = 3
        expected = 0
        actual = min_flips_2(a, b, c)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
