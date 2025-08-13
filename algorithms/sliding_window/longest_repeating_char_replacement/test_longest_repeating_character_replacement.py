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

    def test_aaacbbbaabab(self):
        s = "aaacbbbaabab"
        k = 2
        expected = 6
        actual = character_replacement(s, k)
        self.assertEqual(expected, actual)

    def test_abbcab(self):
        s = "abbcab"
        k = 2
        expected = 5
        actual = character_replacement(s, k)
        self.assertEqual(expected, actual)

    def test_dippitydip(self):
        s = "dippitydip"
        k = 4
        expected = 6
        actual = character_replacement(s, k)
        self.assertEqual(expected, actual)

    def test_coollooc(self):
        s = "coollooc"
        k = 2
        expected = 6
        actual = character_replacement(s, k)
        self.assertEqual(expected, actual)

    def test_aaaaaaaaaa(self):
        s = "aaaaaaaaaa"
        k = 2
        expected = 10
        actual = character_replacement(s, k)
        self.assertEqual(expected, actual)

    def test_lmno(self):
        s = "lmno"
        k = 2
        expected = 3
        actual = character_replacement(s, k)
        self.assertEqual(expected, actual)

    def test_xxxxx(self):
        s = "xxxxx"
        k = 1
        expected = 5
        actual = character_replacement(s, k)
        self.assertEqual(expected, actual)

    def test_fzffz(self):
        s = "fzfzfz"
        k = 6
        expected = 6
        actual = character_replacement(s, k)
        self.assertEqual(expected, actual)

    def test_aabccbb(self):
        s = "aabccbb"
        k = 2
        expected = 5
        actual = character_replacement(s, k)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
