import unittest

from pystrings.encode_decode import encode, decode


class EncodeAndDecodeTestCases(unittest.TestCase):
    def test_encode_lint_code_love_you(self):
        strs = ["lint", "code", "love", "you"]
        expected = ["lint", "code", "love", "you"]

        actual_encode = encode(strs)
        actual_decode = decode(actual_encode)
        self.assertEqual(expected, actual_decode)

    def test_encode_we_say_yes(self):
        strs = ["we", "say", ":", "yes"]
        expected = ["we", "say", ":", "yes"]

        actual_encode = encode(strs)
        actual_decode = decode(actual_encode)
        self.assertEqual(expected, actual_decode)


if __name__ == "__main__":
    unittest.main()
