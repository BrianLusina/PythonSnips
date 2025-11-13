import unittest
from parameterized import parameterized
from . import group_anagrams, group_anagrams_naive


class GroupAnagramsTestCase(unittest.TestCase):
    @parameterized.expand(
        [
            (
                "test_1",
                ["eat", "beat", "neat", "tea"],
                [["eat", "tea"], ["beat"], ["neat"]],
            ),
            (
                "test_2",
                ["duel", "dule", "speed", "spede", "deul", "cars"],
                [["duel", "dule", "deul"], ["speed", "spede"], ["cars"]],
            ),
            (
                "test_3",
                ["eat", "tea", "tan", "ate", "nat", "bat"],
                [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]],
            ),
            (
                "test_4",
                ["word", "sword", "drow", "rowd", "iced", "dice"],
                [["word", "drow", "rowd"], ["sword"], ["iced", "dice"]],
            ),
            (
                "test_5",
                ["eat", "drink", "sleep", "repeat"],
                [["eat"], ["drink"], ["sleep"], ["repeat"]],
            ),
            ("test_6", ["hello", "ohlle", "dark"], [["hello", "ohlle"], ["dark"]]),
        ]
    )
    def test1(self, _, strs, expected):
        actual = group_anagrams(strs)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            (
                "test_1",
                ["eat", "beat", "neat", "tea"],
                [["eat", "tea"], ["beat"], ["neat"]],
            ),
            (
                "test_2",
                ["duel", "dule", "speed", "spede", "deul", "cars"],
                [["duel", "dule", "deul"], ["speed", "spede"], ["cars"]],
            ),
            (
                "test_3",
                ["eat", "tea", "tan", "ate", "nat", "bat"],
                [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]],
            ),
            (
                "test_4",
                ["word", "sword", "drow", "rowd", "iced", "dice"],
                [["word", "drow", "rowd"], ["sword"], ["iced", "dice"]],
            ),
            (
                "test_5",
                ["eat", "drink", "sleep", "repeat"],
                [["eat"], ["drink"], ["sleep"], ["repeat"]],
            ),
            ("test_6", ["hello", "ohlle", "dark"], [["hello", "ohlle"], ["dark"]]),
        ]
    )
    def test2(self, _, strs, expected):
        actual = group_anagrams_naive(strs)
        self.assertEqual(actual, expected)

    def test_1(self):
        strs = ["eat", "beat", "neat", "tea"]
        expected = [["eat", "tea"], ["beat"], ["neat"]]
        actual = group_anagrams(strs)
        self.assertEqual(expected, actual)

    def test_2(self):
        strs = ["duel", "dule", "speed", "spede", "deul", "cars"]
        expected = [["duel", "dule", "deul"], ["speed", "spede"], ["cars"]]
        actual = group_anagrams(strs)
        self.assertEqual(expected, actual)

    def test_3(self):
        strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
        expected = [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
        actual = group_anagrams(strs)
        self.assertEqual(expected, actual)

    def test_4(self):
        strs = ["word", "sword", "drow", "rowd", "iced", "dice"]
        expected = [["word", "drow", "rowd"], ["sword"], ["iced", "dice"]]
        actual = group_anagrams(strs)
        self.assertEqual(expected, actual)

    def test_5(self):
        strs = ["eat", "drink", "sleep", "repeat"]
        expected = [["eat"], ["drink"], ["sleep"], ["repeat"]]
        actual = group_anagrams(strs)
        self.assertEqual(expected, actual)

    def test_6(self):
        strs = ["hello", "ohlle", "dark"]
        expected = [["hello", "ohlle"], ["dark"]]
        actual = group_anagrams(strs)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
