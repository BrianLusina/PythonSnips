import unittest

from pystrings.anagram import Anagrams, is_anagram


class IsAnagramTests(unittest.TestCase):
    def test_fairy_tales_and_rail_safety(self):
        """should return true for s1='fairy tales' and s2='rail safety'"""
        s1 = "fairy tales"
        s2 = "rail safety"
        actual = is_anagram(s1, s2)
        self.assertTrue(actual)

    def test_william_shakespeare_and_i_am_a_weakish_speller(self):
        """should return true for s1='William Shakespeare' and s2='I am a weakish speller'"""
        s1 = "William Shakespeare"
        s2 = "I am a weakish speller"
        actual = is_anagram(s1, s2)
        self.assertTrue(actual)

    def test_madam_curie_and_radium_came(self):
        """should return true for s1='Madam Curie' and s2='Radium came'"""
        s1 = "Madam Curie"
        s2 = "Radium came"
        actual = is_anagram(s1, s2)
        self.assertTrue(actual)


class AnagramTests(unittest.TestCase):
    def setUp(self):
        self.anagram = Anagrams()

    def tearDown(self):
        self.anagram = None

    def test_no_matches(self):
        self.assertEqual(
            [],
            self.anagram.detect_anagrams("diaper", "hello world zombies pants".split()),
        )

    def test_detect_simple_anagram(self):
        self.assertEqual(
            ["tan"], self.anagram.detect_anagrams("ant", "tan stand at".split())
        )

    def test_detect_multiple_anagrams(self):
        self.assertEqual(
            ["stream", "maters"],
            self.anagram.detect_anagrams("master", "stream pigeon maters".split()),
        )

    def test_does_not_confuse_different_duplicates(self):
        self.assertEqual([], self.anagram.detect_anagrams("galea", ["eagle"]))

    def test_eliminate_anagram_subsets(self):
        self.assertEqual([], self.anagram.detect_anagrams("good", "dog goody".split()))

    def test_detect_anagram(self):
        self.assertEqual(
            ["inlets"],
            self.anagram.detect_anagrams(
                "listen", "enlists google inlets banana".split()
            ),
        )

    def test_multiple_anagrams(self):
        self.assertEqual(
            "gallery regally largely".split(),
            self.anagram.detect_anagrams(
                "allergy", "gallery ballerina regally clergy largely leading".split()
            ),
        )

    def test_anagrams_are_case_insensitive(self):
        self.assertEqual(
            ["Carthorse"],
            self.anagram.detect_anagrams(
                "Orchestra", "cashregister Carthorse radishes".split()
            ),
        )

    def test_same_word_isnt_anagram(self):
        self.assertEqual([], self.anagram.detect_anagrams("banana", ["banana"]))

        self.assertEqual([], self.anagram.detect_anagrams("go", "go Go GO".split()))

    def test_detect_no_change_chars(self):
        self.assertEqual(self.anagram.anagram_count("abc", "abc"), 1)

    def test_detect_anagrams_of_self(self):
        self.assertEqual(self.anagram.anagram_count("aab", "baa"), 1)

    def test_child_anagrams(self):
        self.assertEqual(self.anagram.anagram_count("AbrAcadAbRa", "cAda"), 2)

    def test_child_anagrams_2(self):
        self.assertEqual(self.anagram.anagram_count("AdnBndAndBdaBn", "dAn"), 4)

    def test_should_not_fail_with_larger_child(self):
        self.assertEqual(self.anagram.anagram_count("test", "testing"), 0)


if __name__ == "__main__":
    unittest.main()
