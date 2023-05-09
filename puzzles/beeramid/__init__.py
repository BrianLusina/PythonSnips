def beeramid(bonus: int, price: int) -> int:
    """
    Finds the number of levels that can be made from beer cans given the price of a beer can and the total amount of
    money available or the bonus :)

    Complexity Analysis:
       Time Complexity: O(logN) we halve the bonus on each iteration while incrementing the number of levels.
       Space Complexity: O(1) constant space as no extra memory is used. Storing values in variables is negligible
    :param bonus: Bonus
    :param price: Price of a beer can
    :return: the number of levels
    """
    if bonus <= 0:
        return 0

    number_of_cans = bonus // price
    levels = 0

    while (levels + 1) ** 2 <= number_of_cans:
        levels += 1
        number_of_cans -= levels**2

    return levels
