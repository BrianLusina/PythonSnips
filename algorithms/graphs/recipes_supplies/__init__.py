from typing import List, DefaultDict
from collections import defaultdict, deque


def find_recipes(
    recipes: List[str], ingredients: List[List[str]], supplies: List[str]
) -> List[str]:
    # Create a graph to store which recipes depend on which ingredients
    recipe_graph: DefaultDict[str, List[str]] = defaultdict(list)
    # Create a dictionary to keep track of the number of dependencies (indegree) for each recipe
    recipe_in_degrees: DefaultDict[str, int] = defaultdict(int)

    # Initialize a queue with the available supplies
    recipe_queue = deque(supplies)

    # Build the graph and indegree dictionary
    for idx, recipe in enumerate(recipes):
        recipe_ingredients = ingredients[idx]

        for ingredient in recipe_ingredients:
            recipe_in_degrees[recipe] += 1
            recipe_graph[ingredient].append(recipe)

    # List to store the possible recipes that can be made
    possible_recipes: List[str] = []

    # Process the queue until it's empty
    while recipe_queue:
        # Get the next item (ingredient or supply) from the queue
        ingredient = recipe_queue.popleft()

        # Reduce the indegree of all recipes that depend on the current item
        for recipe in recipe_graph[ingredient]:
            recipe_in_degrees[recipe] -= 1
            # If a recipe's indegree reaches 0, all its ingredients are available, so add it to the queue
            if recipe_in_degrees[recipe] == 0:
                possible_recipes.append(recipe)
                recipe_queue.append(recipe)

    return possible_recipes
