# -*- coding: utf-8 -*-
import unittest


class Palindrome(object):
    def __init__(self, n):
        self.n = n

    @staticmethod
    def is_palindrome(a):
        return a == a[::-1]

    @staticmethod
    def longest_palindrome(s):
        s, final_str = s.lower(), ""
        if s == "":
            return 0
        else:
            for y, item in enumerate(s):
                for x, item in enumerate(s):
                    tr = s[y:x + 1]
                    if Palindrome.is_palindrome(tr) and (len(tr) > len(final_str)):
                        final_str = tr

        return len(final_str)


class Tests(unittest.TestCase):
    def single_letter(self):
        self.assertEqual(Palindrome.longest_palindrome("a"), 1)

    def test_double_letter(self):
        self.assertEqual(Palindrome.longest_palindrome("aa"), 2)

    def test_3(self):
        self.assertEqual(Palindrome.longest_palindrome("baa"), 2)

    def test_4(self):
        self.assertEqual(Palindrome.longest_palindrome("aab"), 2)

    def test_5(self):
        self.assertEqual(  Palindrome.longest_palindrome("abcdefghba"), 1)

    def test_6(self):
        self.assertEqual(Palindrome.longest_palindrome("baablkj12345432133d"), 9)
