import unittest

from puzzles.tower_breakers import tower_breakers


class TowerBreakersTestCase(unittest.TestCase):
    def test_n_is_2_and_m_6_returns_2(self):
        """Should return 2 for n=2 and m=6"""
        n = 2
        m = 6
        expected = 2
        actual = tower_breakers(n, m)
        self.assertEqual(expected, actual)

    def test_n_is_2_and_m_is_2_returns_2(self):
        """Should return 2 for n=2 and m=2"""
        n = 2
        m = 2
        expected = 2
        actual = tower_breakers(n, m)
        self.assertEqual(expected, actual)

    def test_n_is_1_and_m_is_4_returns_1(self):
        """Should return 1 for n=1 and m=4"""
        n = 1
        m = 4
        expected = 1
        actual = tower_breakers(n, m)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
