import unittest


def cakes(recipe, available):
    """
    Performs a for loop through the recipe, checks if the ingredient is available, deducts the amount, counts as 1
    :param recipe: ingredients for one cake
    :param available: the ingredients available in the kitchen
    :return: the total cakes that can be baked by the available ingredients
    """
    cake_count = 0
    if len(recipe) > len(available):
        return cake_count
    else:
        if all(x for x in available if x in recipe):
            for x, y in list(tuple(recipe.items())):
                if x in available:
                    available[x] -= recipe[x]
                    print(available)
                    cake_count += 1
    return cake_count


class CakeTests(unittest.TestCase):
    def test_1(self):
        recipe = {"flour": 500, "sugar": 200, "eggs": 1}
        available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
        self.assertEqual(2, cakes(recipe, available))

    def test_2(self):
        recipe = {"flour": 500, "sugar": 200, "eggs": 1}
        available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
        self.assertEqual(2, cakes(recipe, available), "Must return 2")

    def test_3(self):
        recipe = {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}
        available = {"sugar": 500, "flour": 2000, "milk": 2000}
        self.assertEqual(0, cakes(recipe, available), "must return 0")

    def test_4(self):
        recipe = {'flour': 300, 'sugar': 150, 'milk': 100, 'oil': 100, 'cream': 200}
        available = {'flour': 20000, 'oil': 30000, 'cream': 5000, 'milk': 20000, 'sugar': 1700}
        self.assertEqual(11, cakes(recipe, available), "Should equal 11")
