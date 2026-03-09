import unittest

from . import decode_string


class DecodeStringTestCases(unittest.TestCase):
    def test_one(self):
        """should return aaabcbc from 3[a]2[bc]"""
        encoded_string = "3[a]2[bc]"
        expected = "aaabcbc"
        actual = decode_string(encoded_string)
        self.assertEqual(expected, actual)

    def test_two(self):
        """should return aaabcbc from 3[a2[c]]"""
        encoded_string = "3[a2[c]]"
        expected = "accaccacc"
        actual = decode_string(encoded_string)
        self.assertEqual(expected, actual)

    def test_three(self):
        """should return abcabccdcdcdef from 2[abc]3[cd]ef"""
        encoded_string = "2[abc]3[cd]ef"
        expected = "abcabccdcdcdef"
        actual = decode_string(encoded_string)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
