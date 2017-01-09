# -*- coding: utf-8 -*-
import unittest
from pysnips.strings_words.palindrome import Palindrome
from random import choice, randint
from string import ascii_letters


class PalindromeTests(unittest.TestCase):
    def setUp(self):
        self.palindrome = Palindrome()
    
    def single_letter(self):
        
        self.assertEqual(self.palindrome.longest_palindrome("a"), 1)

    def test_double_letter(self):
        self.assertEqual(self.palindrome.longest_palindrome("aa"), 2)

    def test_3(self):
        self.assertEqual(self.palindrome.longest_palindrome("baa"), 2)

    def test_4(self):
        self.assertEqual(self.palindrome.longest_palindrome("aab"), 2)

    def test_5(self):
        self.assertEqual(self.palindrome.longest_palindrome("abcdefghba"), 1)

    def test_6(self):
        self.assertEqual(self.palindrome.longest_palindrome("baablkj12345432133d"), 9)

    def test_7(self):
        self.assertEqual(self.palindrome.is_palindrome("anna"), True)

    def test_8(self):
        self.assertEqual(self.palindrome.is_palindrome("walter"), False)

    def test_9(self):
        self.assertEqual(self.palindrome.is_palindrome(12321), True)

    def test_10(self):
        self.assertEqual(self.palindrome.is_palindrome(123456), False)
        
    def test_one(self):
        self.assertEqual(self.palindrome.palindrome_pairs(["bat", "tab", "cat"]), [[0, 1], [1, 0]])

    def test_two(self):
        self.assertEqual(self.palindrome.palindrome_pairs(["dog", "cow", "tap", "god", "pat"]), [[0, 3], [2, 4], [3, 0], [4, 2]])

    def test_three(self):
        self.assertEqual(self.palindrome.palindrome_pairs(["abcd", "dcba", "lls", "s", "sssll"]), [[0, 1], [1, 0], [2, 4], [3, 2]])

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
            test_case = PalindromeTests.generate_test_case()
            self.assertEqual(self.palindrome.is_palindrome(test_case), self.reference(test_case))
