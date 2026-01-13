import unittest
from typing import List
from parameterized import parameterized
from algorithms.graphs.alien_dictionary import alien_order, alien_order_2

ALIEN_DICTIONARY_TEST_CASES = [
    (["ca", "aa", "ab"], "cab"),
    (["ac", "ab", "zc", "zb"], "cabz"),
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

    @parameterized.expand(ALIEN_DICTIONARY_TEST_CASES)
    def test_alien_order_2(self, words: List[str], expected: str):
        actual = alien_order_2(words)
        self.assertEqual(sorted(expected), sorted(actual))

    def is_valid_alien_order(self, words: List[str], order: str) -> bool:
        if not order:
            return False  # or handle expected empty case separately
        char_rank = {c: i for i, c in enumerate(order)}
        for w1, w2 in zip(words, words[1:]):
            for c1, c2 in zip(w1, w2):
                if c1 != c2:
                    if char_rank.get(c1, -1) > char_rank.get(c2, -1):
                        return False
                    break
            else:
                if len(w1) > len(w2):
                    return False
        return True

if __name__ == "__main__":
    unittest.main()
