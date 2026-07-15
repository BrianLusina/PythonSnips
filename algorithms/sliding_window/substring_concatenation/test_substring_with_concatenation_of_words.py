import unittest
from typing import List
from parameterized import parameterized
from algorithms.sliding_window.substring_concatenation import (
    find_substring,
    find_substring_2,
)

SUBSTRING_WITH_CONCATENATION_OF_WORDS_TEST_CASES = [
    ("barfoothefoobarman", ["foo", "bar"], [0, 9]),
    ("wordgoodgoodgoodbestword", ["word", "good", "best", "word"], []),
    ("barfoofoobarthefoobarman", ["bar", "foo", "the"], [6, 9, 12]),
    ("catcatdogdog", ["cat", "dog"], [3]),
    (
        "lingmindraboofooowingdingbarrwingmonkeypoundcake",
        ["fooo", "barr", "wing", "ding", "wing"],
        [13],
    ),
    ("foobarfoo", ["foo"], [0, 6]),
    ("oneonetwo", ["one", "two"], [3]),
    ("abcdabcabcabcd", ["abc", "abc"], [4, 7]),
]


class SubstringWithConcatenationOfWordsTestCase(unittest.TestCase):
    @parameterized.expand(SUBSTRING_WITH_CONCATENATION_OF_WORDS_TEST_CASES)
    def test_substring_with_concatenation_of_word(
        self, s: str, words: List[str], expected: List[int]
    ):
        actual = find_substring(s, words)
        self.assertEqual(expected, actual)

    @parameterized.expand(SUBSTRING_WITH_CONCATENATION_OF_WORDS_TEST_CASES)
    def test_substring_with_concatenation_of_word_2(
        self, s: str, words: List[str], expected: List[int]
    ):
        actual = find_substring_2(s, words)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
