import unittest

from pystrings.common_ground import common_ground


class CommonGroundTests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(common_ground("eat chicken", "eat chicken and rice"), 'eat chicken')

    def test_2(self):
        self.assertEqual(common_ground("eat a burger and drink a coke", "drink a coke"), 'drink a coke')

    def test_3(self):
        self.assertEqual(common_ground("aa bb", "aa bb cc"), "aa bb")

    def test_4(self):
        self.assertEqual(common_ground("aa bb cc", "bb cc"), 'bb cc')

    def test_5(self):
        self.assertEqual(common_ground("", "cc dd"), 'death')

    def test_6(self):
        self.assertEqual(common_ground("", ""), 'death')

    def test_7(self):
        self.assertEqual(common_ground("aa bb", ""), 'death')

    def test_8(self):
        self.assertEqual(common_ground("i like turtles", "what are you talking about"), 'death')

    def test_9(self):
        self.assertEqual(common_ground("aa bb", "cc dd"), 'death')

    def test_10(self):
        self.assertEqual(common_ground("aa bb cc", "bb cc bb aa"), 'bb cc aa')
