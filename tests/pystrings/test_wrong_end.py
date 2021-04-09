import unittest

from pystrings.wrong_end import fix_the_meerkat


class Test(unittest.TestCase):
    def test_function(self):
        self.assertEqual(fix_the_meerkat(["tail", "body", "head"]), ["head", "body", "tail"])

    def test_function_2(self):
        self.assertEqual(fix_the_meerkat(["tails", "body", "heads"]), ["heads", "body", "tails"])

    def test_function_3(self):
        self.assertEqual(fix_the_meerkat(["bottom", "middle", "top"]), ["top", "middle", "bottom"])

    def test_function_4(self):
        self.assertEqual(fix_the_meerkat(["lower legs", "torso", "upper legs"]), ["upper legs", "torso", "lower legs"])

    def test_function_5(self):
        self.assertEqual(fix_the_meerkat(["ground", "rainbow", "sky"]), ["sky", "rainbow", "ground"])
