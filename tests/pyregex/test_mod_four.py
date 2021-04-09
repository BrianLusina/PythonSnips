import re
import unittest

from pyregex.mod_four import mod


class ModFourTests(unittest.TestCase):
    def test_1(self):
        self.assertIsInstance(mod(""), type(re.compile("")))

    def test_2(self):
        valid_tests = ["[+05620]", "[005624]", "[-05628]", "[005632]", "[555636]", "[+05640]", "[005600]",
                       "the beginning [-0] the end", "~[4]", "[32]",
                       "the beginning [0] ... [invalid] numb[3]rs ... the end",
                       "...may be [+002016] will be."]
        for test in valid_tests:
            self.assertEqual(mod(test) is not None, True)

    def test_3(self):
        invalid_tests = ["[+05621]", "[-55622]",
                         "[005623]", "[~24]", "[8.04]",
                         "No, [2014] isn't a multiple of 4..."]
        for test in invalid_tests:
            self.assertIsNotNone(mod(test))
