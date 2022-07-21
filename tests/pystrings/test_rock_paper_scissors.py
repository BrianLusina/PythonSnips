import unittest

from pystrings.rock_paper_scissors import rps


class RockPaperScissorsTestCase(unittest.TestCase):

    def test_p1_rock_p2_scissors(self):
        p1 = "rock"
        p2 = "scissors"
        expected = "Player 1 won!"
        actual = rps(p1, p2)
        self.assertEqual(expected, actual)

    def test_p1_scissors_p2_rock(self):
        p2 = "rock"
        p1 = "scissors"
        expected = "Player 2 won!"
        actual = rps(p1, p2)
        self.assertEqual(expected, actual)

    def test_p1_rock_p2_rock(self):
        p2 = "rock"
        p1 = "rock"
        expected = "Draw!"
        actual = rps(p1, p2)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
