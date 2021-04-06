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
            for x, _ in tuple(recipe.items()):
                if x in available.keys():
                    available[x] -= recipe[x]
                    cake_count += 1
    return cake_count
