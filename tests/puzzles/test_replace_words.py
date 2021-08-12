import unittest

from puzzles.replace_words import replace_words_with_prefix_hash, replace_words_with_trie


class ReplaceWordsHashTestCases(unittest.TestCase):

    def test_with_cat_bat_rat(self):
        dictionary = ["cat", "bat", "rat"]
        sentence = "the cattle was rattled by the battery"
        expected = "the cat was rat by the bat"
        actual = replace_words_with_prefix_hash(dictionary, sentence)

        self.assertEqual(expected, actual)

    def test_with_a_aa_aaa_aaaa(self):
        dictionary = ["a", "aa", "aaa", "aaaa"]
        sentence = "a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa"
        expected = "a a a a a a a a bbb baba a"
        actual = replace_words_with_prefix_hash(dictionary, sentence)

        self.assertEqual(expected, actual)

    def test_with_a_b_c(self):
        dictionary = ["a", "b", "c"]
        sentence = "aadsfasf absbs bbab cadsfafs"
        expected = "a a b c"
        actual = replace_words_with_prefix_hash(dictionary, sentence)

        self.assertEqual(expected, actual)

    def test_with_catt_cat_bat_rat(self):
        dictionary = ["catt", "cat", "bat", "rat"]
        sentence = "the cattle was rattled by the battery"
        expected = "the cat was rat by the bat"
        actual = replace_words_with_prefix_hash(dictionary, sentence)

        self.assertEqual(expected, actual)

    def test_with_ac_ab(self):
        dictionary = ["ac", "ab"]
        sentence = "it is abnormal that this solution is accepted"
        expected = "it is ab that this solution is ac"
        actual = replace_words_with_prefix_hash(dictionary, sentence)

        self.assertEqual(expected, actual)


class ReplaceWordsHashTrieTestCases(unittest.TestCase):

    def test_with_cat_bat_rat(self):
        dictionary = ["cat", "bat", "rat"]
        sentence = "the cattle was rattled by the battery"
        expected = "the cat was rat by the bat"
        actual = replace_words_with_trie(dictionary, sentence)

        self.assertEqual(expected, actual)

    def test_with_a_aa_aaa_aaaa(self):
        dictionary = ["a", "aa", "aaa", "aaaa"]
        sentence = "a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa"
        expected = "a a a a a a a a bbb baba a"
        actual = replace_words_with_trie(dictionary, sentence)

        self.assertEqual(expected, actual)

    def test_with_a_b_c(self):
        dictionary = ["a", "b", "c"]
        sentence = "aadsfasf absbs bbab cadsfafs"
        expected = "a a b c"
        actual = replace_words_with_trie(dictionary, sentence)

        self.assertEqual(expected, actual)

    def test_with_catt_cat_bat_rat(self):
        dictionary = ["catt", "cat", "bat", "rat"]
        sentence = "the cattle was rattled by the battery"
        expected = "the cat was rat by the bat"
        actual = replace_words_with_trie(dictionary, sentence)

        self.assertEqual(expected, actual)

    def test_with_ac_ab(self):
        dictionary = ["ac", "ab"]
        sentence = "it is abnormal that this solution is accepted"
        expected = "it is ab that this solution is ac"
        actual = replace_words_with_trie(dictionary, sentence)

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
