import unittest
from . import longest_common_subsequence


class LongestCommonSubsequenceTestCase(unittest.TestCase):
    def test_abcde_ace_returns_3(self):
        """should return 3 for text1='abcde' and text2='ace'"""
        text1 = "abcde"
        text2 = "ace"
        expected = 3
        actual = longest_common_subsequence(text1, text2)
        self.assertEqual(expected, actual)

    def test_abc_abc_returns_3(self):
        """should return 3 for text1='abc' and text2='abc'"""
        text1 = "abc"
        text2 = "abc"
        expected = 3
        actual = longest_common_subsequence(text1, text2)
        self.assertEqual(expected, actual)

    def test_abc_def_returns_0(self):
        """should return 0 for text1='abc' and text2='def'"""
        text1 = "abc"
        text2 = "def"
        expected = 0
        actual = longest_common_subsequence(text1, text2)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
