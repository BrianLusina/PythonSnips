# -*- coding: utf-8 -*-
import unittest
from random import choice, randint
from string import ascii_letters


class Palindrome(object):
    def __init__(self, n):
        self.n = n

    @staticmethod
    def is_palindrome(a):
        return str(a) == str(a)[::-1]

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
        self.assertEqual(Palindrome.longest_palindrome("abcdefghba"), 1)

    def test_6(self):
        self.assertEqual(Palindrome.longest_palindrome("baablkj12345432133d"), 9)

    def test_7(self):
        self.assertEqual(Palindrome.is_palindrome("anna"), True)

    def test_8(self):
        self.assertEqual(Palindrome.is_palindrome("walter"), False)

    def test_9(self):
        self.assertEqual(Palindrome.is_palindrome(12321), True)

    def test_10(self):
        self.assertEqual(Palindrome.is_palindrome(123456), False)

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
            self.assertEqual(Palindrome.is_palindrome(test_case), self.reference(test_case))
