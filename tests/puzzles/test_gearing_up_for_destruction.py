import unittest
from puzzles.gearing_up_for_destruction import gearing_up_for_destruction


class GearingUpForDestructionTestCases(unittest.TestCase):
    def test_4_17_50_returns_1_1(self):
        """Should return [-1, -1] for pegs = [4, 17, 50]"""
        pegs = [4, 17, 50]
        expected = [-1, -1]
        actual = gearing_up_for_destruction(pegs)

        self.assertEqual(expected, actual)

    def test_4_30_50_returns_12_1(self):
        """Should return [12, 1] for pegs = [4, 30, 50]"""
        pegs = [4, 30, 50]
        expected = [12, 1]
        actual = gearing_up_for_destruction(pegs)

        self.assertEqual(expected, actual)
        self.assertEqual(expected, actual)

    def test_returns_1_1_for_empty_pegs(self):
        """Should return [-1, -1] for pegs = []"""
        pegs = []
        expected = [-1, -1]
        actual = gearing_up_for_destruction(pegs)

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
