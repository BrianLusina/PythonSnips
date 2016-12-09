import unittest


def square_odds(num_list):
    sq = [str(int(x)**2) for x in num_list.split(",") if int(x) % 2 != 0]
    return ",".join(sq)


class SquareOddTests(unittest.TestCase):
    def test_1(self):
        self.assertEqual("1,9,25,49,81", square_odds("1,2,3,4,5,6,7,8,9"))
