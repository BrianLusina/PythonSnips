import unittest
from pystrings.find_capitals import find_capitals


class FindCapitalsTestCase(unittest.TestCase):
    def test_CodEWaRs(self):
        """CodEWaRs should return [0,3,4,6]"""
        word = "CodEWaRs"
        expected = [0, 3, 4, 6]
        actual = find_capitals(word)
        self.assertEqual(expected, actual)

    def test_uyHIYISqEbkBvrWNXTzsDwCT(self):
        """uyHIYISqEbkBvrWNXTzsDwCT should return [2, 3, 4, 5, 6, 8, 11, 14, 15, 16, 17, 20, 22, 23]"""
        word = "uyHIYISqEbkBvrWNXTzsDwCT"
        expected = [2, 3, 4, 5, 6, 8, 11, 14, 15, 16, 17, 20, 22, 23]
        actual = find_capitals(word)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
