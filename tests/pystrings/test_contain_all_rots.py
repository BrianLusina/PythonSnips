import unittest

from pystrings.contain_all_rots import contain_all_rots


class ContainAllRots(unittest.TestCase):
    def shortDescription(self):
        return "Basic Tests for {}".format(contain_all_rots.__name__)

    def test_1(self):
        self.assertEqual(contain_all_rots("", []), True)

    def test_2(self):
        self.assertEqual(contain_all_rots("", ["bsjq", "qbsj"]), True)

    def test_3(self):
        self.assertEqual(contain_all_rots("bsjq", ["bsjq", "qbsj", "sjqb", "twZNsslC", "jqbs"]), True)

    def test_4(self):
        self.assertEqual(contain_all_rots("XjYABhR",
                                          ["TzYxlgfnhf", "yqVAuoLjMLy", "BhRXjYA", "YABhRXj", "hRXjYAB", "jYABhRX",
                                           "XjYABhR",
                                           "ABhRXjY"]), False)
