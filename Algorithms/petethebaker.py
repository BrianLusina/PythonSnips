import unittest


def cakes(recipe, available):
    # TODO: insert code


class CakeTests(unittest.TestCase):
    def test_1(self):
        recipe = {"flour": 500, "sugar": 200, "eggs": 1}
        available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
        self.assertEqual(2, cakes(recipe,available))