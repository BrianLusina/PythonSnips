import unittest

from . import successful_pairs, successful_pairs_2


class SuccessfulPairsTestCase(unittest.TestCase):
    def test_1(self):
        """spells = [5,1,3], potions = [1,2,3,4,5], success = 7 should return [4,0,3]"""
        spells = [5, 1, 3]
        potions = [1, 2, 3, 4, 5]
        success = 7
        expected = [4, 0, 3]
        actual = successful_pairs(spells, potions, success)
        self.assertEqual(expected, actual)

    def test_2(self):
        """spells = [3,1,2], potions = [8,5,8], success = 16 should return [2,0,2]"""
        spells = [3, 1, 2]
        potions = [8, 5, 8]
        success = 16
        expected = [2, 0, 2]
        actual = successful_pairs(spells, potions, success)
        self.assertEqual(expected, actual)


class SuccessfulPairs2TestCase(unittest.TestCase):
    def test_1(self):
        """spells = [5,1,3], potions = [1,2,3,4,5], success = 7 should return [4,0,3]"""
        spells = [5, 1, 3]
        potions = [1, 2, 3, 4, 5]
        success = 7
        expected = [4, 0, 3]
        actual = successful_pairs_2(spells, potions, success)
        self.assertEqual(expected, actual)

    def test_2(self):
        """spells = [3,1,2], potions = [8,5,8], success = 16 should return [2,0,2]"""
        spells = [3, 1, 2]
        potions = [8, 5, 8]
        success = 16
        expected = [2, 0, 2]
        actual = successful_pairs_2(spells, potions, success)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
