import unittest
from . import reverse_vowels


class ReverseVowerlsTestCase(unittest.TestCase):
    def test_reverse_hello_to_holle(self):
        """should reverse 'hello' to 'holle'"""
        word = "hello"
        expected = "holle"
        actual = reverse_vowels(word)
        self.assertEqual(expected, actual)

    def test_reverse_leetcode_to_leotcede(self):
        """should reverse 'leetcode' to 'leotcede'"""
        word = "leetcode"
        expected = "leotcede"
        actual = reverse_vowels(word)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
