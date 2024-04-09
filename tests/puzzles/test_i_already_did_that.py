import unittest

from puzzles.hey_i_already_did_that import hey_i_already_did_that


class HeyIAlreadyDidThatTestCases(unittest.TestCase):
    def test_n_of_210022_and_base_3_returns_3(self):
        """Should return 3 for n = '210022' and base = 3"""
        n = "210022"
        b = 3
        expected = 3
        actual = hey_i_already_did_that(n, b)

        self.assertEqual(expected, actual)

    def test_n_of_1211_and_base_10_returns_1(self):
        """Should return 1 for n = '1211' and base = 10"""
        n = "1211"
        b = 10
        expected = 1
        actual = hey_i_already_did_that(n, b)

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
