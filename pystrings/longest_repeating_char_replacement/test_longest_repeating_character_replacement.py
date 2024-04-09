import unittest

from . import character_replacement


class LongestRepeatingCharacterReplacementTestCase(unittest.TestCase):
    def test_ABAB_with_2(self):
        """ABAB with k =2 should return 4"""
        s = "ABAB"
        k = 2
        expected = 4
        actual = character_replacement(s, k)
        self.assertEqual(expected, actual)

    def test_AABABBA_with_1(self):
        """AABABBA with k = 1 should return 4"""
        s = "AABABBA"
        k = 1
        expected = 4
        actual = character_replacement(s, k)
        self.assertEqual(expected, actual)

    def test_ABCCDC_with_1(self):
        """ABCCDC with k = 1 should return 4"""
        s = "ABCCDC"
        k = 1
        expected = 4
        actual = character_replacement(s, k)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
