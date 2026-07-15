import unittest

from . import knight


class KnightChessBoardTestCase(unittest.TestCase):
    def test_1(self):
        """should return 6 for A = 8, B = 8, C = 1, D = 1, E = 8,F = 8"""
        a = 8
        b = 8
        c = 1
        d = 1
        e = 8
        f = 8
        actual = knight(
            rows=a, cols=b, initial_x=c, initial_y=d, destination_x=e, destination_y=f
        )
        expected = 6
        self.assertEqual(expected, actual)

    def test_2(self):
        """should return 2 for A : 4 B : 7 C : 2 D : 6 E : 2 F : 4"""
        a = 4
        b = 7
        c = 2
        d = 6
        e = 2
        f = 4
        actual = knight(
            rows=a, cols=b, initial_x=c, initial_y=d, destination_x=e, destination_y=f
        )
        expected = 2
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
