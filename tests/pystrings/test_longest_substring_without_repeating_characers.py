import unittest
from pystrings.longest_substring_without_repeating_characters import length_of_longest_substring


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


if __name__ == '__main__':
    unittest.main()
