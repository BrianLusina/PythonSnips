from unittest import TestCase

from pystrings.random_caser import random_case


class RandomCaseTestCases(TestCase):
    def test_1(self):
        i = "this is an all lower string"
        r = random_case(i)
        self.assertNotEqual(r, i.lower())

    def test_2(self):
        i = "Lorem ipsum dolor sit amet, consectetur adipiscing elit"
        r = random_case(i)
        self.assertEqual(r.lower(), i.lower())

    def test_3(self):
        i = "Donec eleifend cursus lobortis"
        r = random_case(i)
        self.assertNotEqual(r, i)

    def test_4(self):
        i = "THIS IS AN ALL CAPS STRING"
        r = random_case(i)
        self.assertNotEqual(r, i.upper())
