# -*- coding: utf-8 -*-
import unittest
from pysnips.strings_words.palindrome import is_palindrome, longest_palindrome
from random import choice, randint
from string import ascii_letters


class Tests(unittest.TestCase):
    def single_letter(self):
        self.assertEqual(longest_palindrome("a"), 1)

    def test_double_letter(self):
        self.assertEqual(longest_palindrome("aa"), 2)

    def test_3(self):
        self.assertEqual(longest_palindrome("baa"), 2)

    def test_4(self):
        self.assertEqual(longest_palindrome("aab"), 2)

    def test_5(self):
        self.assertEqual(longest_palindrome("abcdefghba"), 1)

    def test_6(self):
        self.assertEqual(longest_palindrome("baablkj12345432133d"), 9)

    def test_7(self):
        self.assertEqual(is_palindrome("anna"), True)

    def test_8(self):
        self.assertEqual(is_palindrome("walter"), False)

    def test_9(self):
        self.assertEqual(is_palindrome(12321), True)

    def test_10(self):
        self.assertEqual(is_palindrome(123456), False)

    @staticmethod
    def generate_test_case():
        if randint(0, 1000):
            test_case = randint(0, 10000000)
        else:
            test_case = "".join(choice(ascii_letters) for _ in range(randint(1, 1000)))
            if randint(0, 1000):
                test_case = "%s%s" % (test_case, test_case[::-1])

        return test_case

    @staticmethod
    def reference(s):
        return str(s) == str(s)[::-1]

    def test_11(self):
        for _ in range(100):
            test_case = Tests.generate_test_case()
            self.assertEqual(is_palindrome(test_case), self.reference(test_case))
