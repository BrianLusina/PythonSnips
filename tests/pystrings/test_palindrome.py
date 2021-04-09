# -*- coding: utf-8 -*-
import unittest
from random import choice, randint
from string import ascii_letters

from pystrings.palindrome import Palindrome


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

    def test_palindrome_pairs_1(self):
        self.assertEqual(self.palindrome.palindrome_pairs(["bat", "tab", "cat"]), [[0, 1], [1, 0]])

    def test_palindrome_pairs_2(self):
        self.assertEqual(self.palindrome.palindrome_pairs(["dog", "cow", "tap", "god", "pat"]),
                         [[0, 3], [2, 4], [3, 0], [4, 2]])

    def test_palindrome_pairs_3(self):
        self.assertEqual(self.palindrome.palindrome_pairs(["abcd", "dcba", "lls", "s", "sssll"]),
                         [[0, 1], [1, 0], [2, 4], [3, 2]])

    def test_largest_palindrome_from_single_digit_factors(self):
        value, factors = self.palindrome.largest_palindrome(max_factor=9)
        self.assertEqual(9, value)
        self.assertIn(set(factors), [{1, 9}, {3, 3}])

    def test_largest_palindrome_from_double_digit_factors(self):
        value, factors = self.palindrome.largest_palindrome(max_factor=99, min_factor=10)
        self.assertEqual(9009, value)
        self.assertEqual({91, 99}, set(factors))

    def test_smallest_palindrome_from_double_digit_factors(self):
        value, factors = self.palindrome.smallest_palindrome(max_factor=99, min_factor=10)
        self.assertEqual(121, value)
        self.assertEqual({11}, set(factors))

    def test_largest_palindrome_from_triple_digit_factors(self):
        value, factors = self.palindrome.largest_palindrome(max_factor=999, min_factor=100)
        self.assertEqual(906609, value)
        self.assertEqual({913, 993}, set(factors))

    def test_smallest_palindrome_from_triple_digit_factors(self):
        value, factors = self.palindrome.smallest_palindrome(max_factor=999, min_factor=100)
        self.assertEqual(10201, value)
        self.assertEqual({101, 101}, set(factors))

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

    def test_14(self):
        for _ in range(100):
            test_case = PalindromeTests.generate_test_case()
            self.assertEqual(self.palindrome.is_palindrome(test_case), self.reference(test_case))


if __name__ == '__main__':
    unittest.main()
