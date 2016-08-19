import unittest
import re


class CapsTests(unittest.TestCase):
    def test_hello(self):
        self.assertEqual({'UPPER CASE': 1,"LOWER CASE": 9}, "Hello world!",)
