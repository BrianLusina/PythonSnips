import unittest
from typing import List
from parameterized import parameterized
from algorithms.graphs.recipes_supplies import find_recipes

FIND_ALL_POSSIBLE_RECIPES_TEST_CASES = [
    (
        ["tea", "omelette"],
        [["milk", "caffeine", "sugar"], ["salt", "egg", "pepper"]],
        ["salt", "milk", "egg", "caffeine", "sugar"],
        ["tea"],
    ),
    (
        ["sandwich", "mojito"],
        [["cheese", "vegetables", "bread", "salad"], ["rum", "mint", "syrup"]],
        ["cheese", "rum", "bread", "salad", "vegetables", "mint", "syrup"],
        ["sandwich", "mojito"],
    ),
    (
        ["bread", "sandwich", "burger"],
        [["yeast", "flour"], ["bread", "meat"], ["sandwich", "meat", "bread"]],
        ["yeast", "flour", "meat"],
        ["bread", "sandwich", "burger"],
    ),
    (
        ["bread", "sandwich"],
        [["yeast", "flour"], ["bread", "meat"]],
        ["yeast", "flour", "meat"],
        ["bread", "sandwich"],
    ),
    (
        ["bread"],
        [["yeast", "flour"]],
        ["yeast", "flour", "corn"],
        ["bread"],
    ),
    (
        ["pasta", "egg", "chicken"],
        [["yeast", "flour"], ["pasta", "meat"], ["egg", "meat", "pasta"]],
        ["yeast", "flour", "meat"],
        ["pasta", "egg", "chicken"],
    ),
    (
        ["custard", "trifle"],
        [
            ["yeast", "flour", "trifle", "bananas", "eggs", "milk"],
            ["eggs", "milk", "custard"],
        ],
        ["eggs", "milk", "yeast", "flour", "corn", "bananas"],
        [],
    ),
]


class FindAllPossibleRecipesTestCase(unittest.TestCase):
    @parameterized.expand(FIND_ALL_POSSIBLE_RECIPES_TEST_CASES)
    def test_find_recipes(
        self,
        recipies: List[str],
        ingredients: List[List[str]],
        supplies: List[str],
        expected: List[str],
    ):
        actual = find_recipes(recipies, ingredients, supplies)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
