# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
from typing import Optional
from parameterized import parameterized
from algorithms.strings.run_length_encoding import decode, encode


RUN_LENGTH_ENCODING_TEST_CASES = [
    ("AABBBCCCC", None, "2A3B4C"),
    ("WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB", None, "12WB12W3B24WB"),
    ("⏰⚽⚽⚽⭐⭐⏰", None, "⏰3⚽2⭐⏰"),
    ("AAAAAAAAAAAAABBCCCCDD", 10, "9A4A2B4C2D"),
]

RUN_LENGTH_DECODING_TEST_CASES = [
    ("2A3B4C", "AABBBCCCC"),
    ("12WB12W3B24WB", "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB"),
    ("⏰3⚽2⭐⏰", "⏰⚽⚽⚽⭐⭐⏰"),
]


class RunLengthEncodingDecodingTests(unittest.TestCase):
    @parameterized.expand(RUN_LENGTH_ENCODING_TEST_CASES)
    def test_encode(self, text: str, limit: Optional[int], expected: str):
        actual = encode(text, limit)
        self.assertEqual(actual, expected)

    @parameterized.expand(RUN_LENGTH_DECODING_TEST_CASES)
    def test_decode(self, text: str, expected: str):
        actual = decode(text)
        self.assertEqual(actual, expected)

    def test_combination(self):
        self.assertMultiLineEqual("zzz ZZ  zZ", decode(encode("zzz ZZ  zZ")))


if __name__ == "__main__":
    unittest.main()
