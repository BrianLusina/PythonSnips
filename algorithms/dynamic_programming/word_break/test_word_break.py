import unittest
from typing import List
from parameterized import parameterized
from algorithms.dynamic_programming.word_break import word_break_trie, word_break_dp, word_break_dp_2


class WordBreakTestCases(unittest.TestCase):
    @parameterized.expand(
        [
            (
                "magiclly",
                ["ag", "al", "icl", "mag", "magic", "ly", "lly"],
                ["mag icl ly", "magic lly"],
            ),
            (
                "raincoats",
                ["rain", "oats", "coat", "s", "rains", "oat", "coats", "c"],
                ["rain c oats", "rain c oat s", "rain coats", "rain coat s"],
            ),
            (
                "highway",
                ["crash", "cream", "high", "highway", "low", "way"],
                ["highway", "high way"],
            ),
            ("robocat", ["rob", "cat", "robo", "bo", "b"], ["robo cat"]),
            (
                "cocomomo",
                ["co", "mo", "coco", "momo"],
                ["co co momo", "co co mo mo", "coco momo", "coco mo mo"],
            ),
            (
                "catsanddog",
                ["cat", "cats", "and", "sand", "dog"],
                ["cats and dog", "cat sand dog"],
            ),
            (
                "pineapplepenapple",
                ["apple", "pen", "applepen", "pine", "pineapple"],
                ["pine apple pen apple", "pineapple pen apple", "pine applepen apple"],
            ),
            ("catsandog", ["cats", "dog", "sand", "and", "cat"], []),
        ]
    )
    def test_word_break_trie(self, s: str, word_dict: List[str], expected: List[str]):
        actual = word_break_trie(s, word_dict)
        actual.sort()
        expected.sort()
        self.assertListEqual(expected, actual)

    @parameterized.expand(
        [
            (
                "magiclly",
                ["ag", "al", "icl", "mag", "magic", "ly", "lly"],
                ["mag icl ly", "magic lly"],
            ),
            (
                "raincoats",
                ["rain", "oats", "coat", "s", "rains", "oat", "coats", "c"],
                ["rain c oats", "rain c oat s", "rain coats", "rain coat s"],
            ),
            (
                "highway",
                ["crash", "cream", "high", "highway", "low", "way"],
                ["highway", "high way"],
            ),
            ("robocat", ["rob", "cat", "robo", "bo", "b"], ["robo cat"]),
            (
                "cocomomo",
                ["co", "mo", "coco", "momo"],
                ["co co momo", "co co mo mo", "coco momo", "coco mo mo"],
            ),
            (
                "catsanddog",
                ["cat", "cats", "and", "sand", "dog"],
                ["cats and dog", "cat sand dog"],
            ),
            (
                "pineapplepenapple",
                ["apple", "pen", "applepen", "pine", "pineapple"],
                ["pine apple pen apple", "pineapple pen apple", "pine applepen apple"],
            ),
            ("catsandog", ["cats", "dog", "sand", "and", "cat"], []),
        ]
    )
    def test_word_break_dp(self, s: str, word_dict: List[str], expected: List[str]):
        actual = word_break_dp(s, word_dict)
        actual.sort()
        expected.sort()
        self.assertListEqual(expected, actual)

    @parameterized.expand(
        [
            (
                "magiclly",
                ["ag", "al", "icl", "mag", "magic", "ly", "lly"],
                ["mag icl ly", "magic lly"],
            ),
            (
                "raincoats",
                ["rain", "oats", "coat", "s", "rains", "oat", "coats", "c"],
                ["rain c oats", "rain c oat s", "rain coats", "rain coat s"],
            ),
            (
                "highway",
                ["crash", "cream", "high", "highway", "low", "way"],
                ["highway", "high way"],
            ),
            ("robocat", ["rob", "cat", "robo", "bo", "b"], ["robo cat"]),
            (
                "cocomomo",
                ["co", "mo", "coco", "momo"],
                ["co co momo", "co co mo mo", "coco momo", "coco mo mo"],
            ),
            (
                "catsanddog",
                ["cat", "cats", "and", "sand", "dog"],
                ["cats and dog", "cat sand dog"],
            ),
            (
                "pineapplepenapple",
                ["apple", "pen", "applepen", "pine", "pineapple"],
                ["pine apple pen apple", "pineapple pen apple", "pine applepen apple"],
            ),
            ("catsandog", ["cats", "dog", "sand", "and", "cat"], []),
        ]
    )
    def test_word_break_dp_2(self, s: str, word_dict: List[str], expected: List[str]):
        actual = word_break_dp_2(s, word_dict)
        actual.sort()
        expected.sort()
        self.assertListEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
