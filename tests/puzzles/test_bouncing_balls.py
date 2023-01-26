import unittest
from puzzles.bouncing_balls import bouncing_ball


class BouncingBallsTestCase(unittest.TestCase):
    def test_one(self):
        """h = 2, bounce = 0.5, window=1 should return 1"""
        h = 2
        bounce = 0.5
        window = 1
        expected = 1
        actual = bouncing_ball(h, bounce, window)
        self.assertEqual(expected, actual)

    def test_two(self):
        """h = 3, bounce = 0.66, window=1.5 should return 3"""
        h = 3
        bounce = 0.66
        window = 1.5
        expected = 3
        actual = bouncing_ball(h, bounce, window)
        self.assertEqual(expected, actual)

    def test_three(self):
        """h = 30, bounce = 0.66, window=1.5 should return 15"""
        h = 30
        bounce = 0.66
        window = 1.5
        expected = 15
        actual = bouncing_ball(h, bounce, window)
        self.assertEqual(expected, actual)

    def test_four(self):
        """h = 30, bounce = 0.75, window=1.5 should return 21"""
        h = 30
        bounce = 0.75
        window = 1.5
        expected = 21
        actual = bouncing_ball(h, bounce, window)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
