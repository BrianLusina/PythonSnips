def beeramid(bonus, price):
    if bonus <= 0:
        return 0

    number_of_cans = bonus // price
    levels = 0

    while (levels + 1) ** 2 <= number_of_cans:
        levels += 1
        number_of_cans -= levels ** 2

    return levels
