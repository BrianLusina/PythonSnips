import unittest

from pystrings.remove_all_adjacent_duplicates import remove_duplicates


class RemoveAllAdjacentDuplicatesTestCase(unittest.TestCase):
    def test_abbaca_returns_ca(self):
        """should return ca for abbaca"""
        word = "abbaca"
        expected = "ca"
        actual = remove_duplicates(word)
        self.assertEqual(expected, actual)

    def test_azxxzy_returns_ay(self):
        """should return ay for azxxzy"""
        word = "azxxzy"
        expected = "ay"
        actual = remove_duplicates(word)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
