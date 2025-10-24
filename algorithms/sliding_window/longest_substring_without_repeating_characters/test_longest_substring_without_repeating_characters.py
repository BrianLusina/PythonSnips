import unittest
from . import length_of_longest_substring


class LongestSubstringWithoutRepeatingCharactersTestCase(unittest.TestCase):
    def test_abcabcbb(self):
        """abcabcbb should return 3"""
        s = "abcabcbb"
        expected = 3
        actual = length_of_longest_substring(s)
        self.assertEqual(expected, actual)

    def test_bbbbb(self):
        """bbbbb should return 1"""
        s = "bbbbb"
        expected = 1
        actual = length_of_longest_substring(s)
        self.assertEqual(expected, actual)

    def test_pwwkew(self):
        """pwwkew should return 3"""
        s = "pwwkew"
        expected = 3
        actual = length_of_longest_substring(s)
        self.assertEqual(expected, actual)

    def test_bbbbbb(self):
        """bbbbbb should return 1"""
        s = "bbbbbb"
        expected = 1
        actual = length_of_longest_substring(s)
        self.assertEqual(expected, actual)

    def test_empty_string(self):
        """'' should return 0"""
        s = ""
        expected = 0
        actual = length_of_longest_substring(s)
        self.assertEqual(expected, actual)

    def test_abcdbea(self):
        """abcdbea should return 5"""
        s = "abcdbea"
        expected = 5
        actual = length_of_longest_substring(s)
        self.assertEqual(expected, actual)

    def test_aba(self):
        """aba should return 2"""
        s = "aba"
        expected = 2
        actual = length_of_longest_substring(s)
        self.assertEqual(expected, actual)

    def test_abccabcabcc(self):
        """abccabcabcc should return 3"""
        s = "abccabcabcc"
        expected = 3
        actual = length_of_longest_substring(s)
        self.assertEqual(expected, actual)

    def test_aaaabaaa(self):
        """aaaabaaa should return 2"""
        s = "aaaabaaa"
        expected = 2
        actual = length_of_longest_substring(s)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
