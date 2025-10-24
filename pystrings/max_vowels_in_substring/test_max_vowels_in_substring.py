import unittest
from . import max_vowels


class MaxVowelsInSubstringTestCase(unittest.TestCase):
    def test_s_is_abciiidef_and_k_is_3(self):
        """should return 3 from s = "abciiidef", k = 3"""
        s = "abciiidef"
        k = 3
        expected = 3
        actual = max_vowels(s, k)
        self.assertEqual(expected, actual)

    def test_s_is_aeiou_and_k_is_2(self):
        """should return 2 from s = "aeiou", k = 2"""
        s = "aeiou"
        k = 2
        expected = 2
        actual = max_vowels(s, k)
        self.assertEqual(expected, actual)

    def test_s_is_leetcode_and_k_is_3(self):
        """should return 2 from s = "leetcode", k = 3"""
        s = "leetcode"
        k = 3
        expected = 2
        actual = max_vowels(s, k)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
