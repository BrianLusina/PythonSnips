import unittest
from . import longest_common_suffix_queries


class LongestCommonSuffixQueriesTestCase(unittest.TestCase):
    def test_1(self):
        """should return [1,1,1] for words_container=["mango","ango","xango"] and words_query=["go","ango","xyz"]"""
        words_container = ["mango", "ango", "xango"]
        words_query = ["go", "ango", "xyz"]
        expected = [1, 1, 1]
        actual = longest_common_suffix_queries(
            words_container=words_container, words_query=words_query
        )
        self.assertEqual(expected, actual)

    def test_2(self):
        """should return [0,0,0] for words_container=["flight", "night", "tight", "light"] and words_query=["ight","t","zzz"]"""
        words_container = ["flight", "night", "tight", "light"]
        words_query = ["ight", "t", "zzz"]
        expected = [1, 1, 1]
        actual = longest_common_suffix_queries(
            words_container=words_container, words_query=words_query
        )
        self.assertEqual(expected, actual)

    def test_3(self):
        """should return [1,1,0] for words_container=["hello", "yellow", "mellow", "fellow"] and words_query=["low", "ellow", "wow"]"""
        words_container = ["hello", "yellow", "mellow", "fellow"]
        words_query = ["low", "ellow", "wow"]
        expected = [1, 1, 1]
        actual = longest_common_suffix_queries(
            words_container=words_container, words_query=words_query
        )
        self.assertEqual(expected, actual)

    def test_4(self):
        """should return [3,3,3] for words_container=["cat", "start", "part", "art"] and words_query=["art", "rt", "xyz"]"""
        words_container = ["cat", "start", "part", "art"]
        words_query = ["art", "rt", "xyz"]
        expected = [3, 3, 0]
        actual = longest_common_suffix_queries(
            words_container=words_container, words_query=words_query
        )
        self.assertEqual(expected, actual)

    def test_5(self):
        """should return [0,1,2] for words_container=["abcde", "bcde", "cde"] and words_query=["abcde", "bcde", "cde"]"""
        words_container = ["abcde", "bcde", "cde"]
        words_query = ["abcde", "bcde", "cde"]
        expected = [0, 1, 2]
        actual = longest_common_suffix_queries(
            words_container=words_container, words_query=words_query
        )
        self.assertEqual(expected, actual)

    def test_6(self):
        """should return [2,2,2] for words_container=["starting","sting","ring"] and words_query=["ring","ing","random"]"""
        words_container = ["starting", "sting", "ring"]
        words_query = ["ring", "ing", "random"]
        expected = [2, 2, 2]
        actual = longest_common_suffix_queries(
            words_container=words_container, words_query=words_query
        )
        self.assertEqual(expected, actual)

    def test_7(self):
        """should return [1,1,1] for words_container=["alpha","beta","gamma"] and words_query=["ta","eta","zeta"]"""
        words_container = ["alpha", "beta", "gamma"]
        words_query = ["ta", "eta", "zeta"]
        expected = [1, 1, 1]
        actual = longest_common_suffix_queries(
            words_container=words_container, words_query=words_query
        )
        self.assertEqual(expected, actual)

    def test_8(self):
        """should return [2,2,2] for words_container=["respect","aspect","spect"] and words_query=["spect","ect","detect"]"""
        words_container = ["respect", "aspect", "spect"]
        words_query = ["spect", "ect", "detect"]
        expected = [2, 2, 2]
        actual = longest_common_suffix_queries(
            words_container=words_container, words_query=words_query
        )
        self.assertEqual(expected, actual)

    def test_9(self):
        """should return [2,0,2] for words_container=["abcdefgh","poiuygh","ghghgh"] and words_query=["gh","acbfgh","acbfegh"]"""
        words_container = ["abcdefgh", "poiuygh", "ghghgh"]
        words_query = ["gh", "acbfgh", "acbfegh"]
        expected = [2, 0, 2]
        actual = longest_common_suffix_queries(
            words_container=words_container, words_query=words_query
        )
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
