import unittest
from typing import List
from parameterized import parameterized
from algorithms.backtracking.permutations.generate_permutations import (
    generate_permutations,
    permute_word,
)

GENERATE_PERMUTATIONS_TEST_CASES = [
    ("a", ["a"]),
    ("ab", ["ab", "ba"]),
    ("abc", ["abc", "acb", "bac", "bca", "cab", "cba"]),
    (
        "abcd",
        [
            "abcd",
            "abdc",
            "acbd",
            "acdb",
            "adbc",
            "adcb",
            "bacd",
            "badc",
            "bcad",
            "bcda",
            "bdac",
            "bdca",
            "cabd",
            "cadb",
            "cbad",
            "cbda",
            "cdab",
            "cdba",
            "dabc",
            "dacb",
            "dbac",
            "dbca",
            "dcab",
            "dcba",
        ],
    ),
    ("bad", ["abd", "adb", "bad", "bda", "dab", "dba"]),
    ("xyz", ["xyz", "xzy", "yxz", "yzx", "zxy", "zyx"]),
]


class GenerateAllPermutationsTestCase(unittest.TestCase):
    @parameterized.expand(GENERATE_PERMUTATIONS_TEST_CASES)
    def test_generate_permutations(self, word: str, expected: List[str]):
        actual = generate_permutations(word)
        self.assertListEqual(sorted(expected), sorted(actual))

    @parameterized.expand(GENERATE_PERMUTATIONS_TEST_CASES)
    def test_permute_word(self, word: str, expected: List[str]):
        actual = permute_word(word)
        self.assertListEqual(sorted(expected), sorted(actual))


if __name__ == "__main__":
    unittest.main()
