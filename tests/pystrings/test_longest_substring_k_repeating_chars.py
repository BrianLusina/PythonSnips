import unittest

from pystrings.longest_substring_with_k_repeating_chars import longest_substring


class LongestSubstringWithKRepeatingCharsTestCase(unittest.TestCase):
    def test_aaabb(self):
        expected = 3
        self.assertEqual(expected, longest_substring("aaabb", 3))

    def test_ababacb(self):
        expected = 0
        self.assertEqual(expected, longest_substring("ababacb", 3))


if __name__ == '__main__':
    unittest.main()
