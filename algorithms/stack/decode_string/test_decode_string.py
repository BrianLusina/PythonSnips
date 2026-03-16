import unittest
from parameterized import parameterized
from algorithms.stack.decode_string import decode_string, decode_string_2

DECODE_STRING_TEST_CASES = [
    ("3[a]2[bc]", "aaabcbc"),
    ("3[a2[c]]", "accaccacc"),
    ("2[abc]3[cd]ef", "abcabccdcdcdef"),
    ("1[abc]2[def]3[ghi]", "abcdefdefghighighi"),
    ("1[a2[b3[c4[d]]]]", "abcddddcddddcddddbcddddcddddcdddd"),
]


class DecodeStringTestCases(unittest.TestCase):
    @parameterized.expand(DECODE_STRING_TEST_CASES)
    def test_decode_string(self, encoded_string: str, expected: str):
        actual = decode_string(encoded_string)
        self.assertEqual(expected, actual)

    @parameterized.expand(DECODE_STRING_TEST_CASES)
    def test_decode_string_2(self, encoded_string: str, expected: str):
        actual = decode_string_2(encoded_string)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
