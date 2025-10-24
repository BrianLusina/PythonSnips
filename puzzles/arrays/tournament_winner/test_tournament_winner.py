import unittest
from . import tournament_winner

class TournamentWinnerTestCase(unittest.TestCase):
    def test_1(self):
        competitions = [["HTML", "C#"], ["C#", "Python"], ["Python", "HTML"]]
        results = [0, 0, 1]
        expected = "Python"
        actual = tournament_winner(competitions, results)
        self.assertEqual(expected, actual)

    def test_2(self):
        competitions = [["HTML", "Java"],["Java", "Python"],["Python", "HTML"]]
        results = [0, 1, 1]
        expected = "Java"
        actual = tournament_winner(competitions, results)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
