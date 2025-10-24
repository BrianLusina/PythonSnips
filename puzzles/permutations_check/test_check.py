import unittest

from . import check


class CheckTestCase(unittest.TestCase):
    def test_1(self):
        """should return True for  n = 2, m = 1, games=[[1, 2]]"""
        n = 2
        m = 1
        games = [[1, 2]]
        actual = check(n, m, games)
        self.assertTrue(actual)

    def test_2(self):
        """should return False for  n = 4, m = 2, games=[[1, 2, 3, 4], [4,3,1,2]]"""
        n = 4
        m = 2
        games = [[1, 2, 3, 4], [4, 3, 1, 2]]
        actual = check(n, m, games)
        self.assertFalse(actual)

    def test_3(self):
        """should return False for  n = 4, m = 2, games=[[1, 2, 3, 4], [1, 3, 2, 4]]"""
        n = 4
        m = 2
        games = [[1, 2, 3, 4], [1, 3, 2, 4]]
        actual = check(n, m, games)
        self.assertTrue(actual)

    def test_4(self):
        """should return False for n = 6, m = 6, games=[[1, 6, 4, 5, 2], [6, 4, 2, 3, 1, 5], [4, 2, 1, 5, 6, 3], [4, 5, 1, 6, 2, 3], [3, 2, 5, 1, 6, 4],
                 [2, 3, 6, 4, 1, 5]]"""
        n = 6
        m = 6
        games = [[1, 6, 4, 5, 2], [6, 4, 2, 3, 1, 5], [4, 2, 1, 5, 6, 3], [4, 5, 1, 6, 2, 3], [3, 2, 5, 1, 6, 4],
                 [2, 3, 6, 4, 1, 5]]
        actual = check(n, m, games)
        self.assertTrue(actual)

    def test_5(self):
        """should return False for n = 6, m = 6, games=[[3, 1, 4, 5, 6, 2], [5, 3, 2, 4, 1, 6], [5, 3, 6, 4, 2, 1], [6, 5, 3, 2, 1, 4], [5, 4, 1, 2, 6, 3],
                 [4, 1, 6, 2, 5, 3]]"""
        n = 6
        m = 6
        games = [[3, 1, 4, 5, 6, 2], [5, 3, 2, 4, 1, 6], [5, 3, 6, 4, 2, 1], [6, 5, 3, 2, 1, 4], [5, 4, 1, 2, 6, 3],
                 [4, 1, 6, 2, 5, 3]]
        actual = check(n, m, games)
        self.assertFalse(actual)


if __name__ == '__main__':
    unittest.main()
