import unittest
import re


def caps_counter(word):
    result = {"UPPER CASE": 0, "LOWER CASE": 0}
    for x in word:
        if re.match(r"[A-Z]", x):
            result["UPPER CASE"] += 1
        elif re.match(r'[a-z]', x):
            result['LOWER CASE'] += 1
    return result


class CapsTests(unittest.TestCase):
    def test_hello(self):
        self.assertEqual({'UPPER CASE': 1, "LOWER CASE": 9}, caps_counter("Hello world!"))

    def test_2(self):
        self.assertEqual({'UPPER CASE': 6, "LOWER CASE": 20}, caps_counter("me and them and me and you MEEEND"))

    def test_punctuation_only(self):
        self.assertEqual({"UPPER CASE": 0, "LOWER CASE": 0}, caps_counter(",./@#][{}~@>?"))
