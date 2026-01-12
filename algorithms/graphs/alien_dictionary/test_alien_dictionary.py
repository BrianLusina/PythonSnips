import unittest
from typing import List
from parameterized import parameterized
from algorithms.graphs.alien_dictionary import alien_order

ALIEN_DICTIONARY_TEST_CASES = [
    (["ca", "aa", "ab"], "cab"),  # Passes
    (["ac", "ab", "zc", "zb"], "cabz"),  #
    (["baa", "abcd", "abca", "cab", "cad"], "bdac"),
    (["mdx", "mars", "avgd", "dkae"], ""),
    (["m", "a", "b", "s"], "mabs"),
    (["xro", "xma", "per", "prt", "oxh", "olv"], "xaethvlprom"),
    (["o", "l", "m", "s"], "olms"),
    (
        [
            "mdxok",
            "mrolw",
            "mroqs",
            "kptz",
            "klr",
            "klon",
            "zvef",
            "zrsu",
            "zzs",
            "orm",
            "oqt",
        ],
        "mdxwsptnvefuklrzqo",
    ),
    (
        [
            "m",
            "mx",
            "mxe",
            "mxer",
            "mxerl",
            "mxerlo",
            "mxerlos",
            "mxerlost",
            "mxerlostr",
            "mxerlostrpq",
            "mxerlostrp",
        ],
        "",
    ),
    (["wgencorejikhdiwnbhx"], "wgencorjikhdbx"),
]


class AlienDictionaryTestCase(unittest.TestCase):
    @parameterized.expand(ALIEN_DICTIONARY_TEST_CASES)
    def test_alien_order(self, words: List[str], expected: str):
        actual = alien_order(words)
        self.assertEqual(sorted(expected), sorted(actual))


if __name__ == "__main__":
    unittest.main()
