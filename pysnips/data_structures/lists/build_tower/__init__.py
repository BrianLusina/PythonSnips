def tower_builder(n_floors):
    """
    Takes in an integer and builds a tower of * from the given int
    :param n_floors: the number of floors for the tower
    :return: a list with the number of floors represented with *
    :rtype: list
    """
    return [("*" * (i * 2 - 1)).center(n_floors * 2 - 1)
            for i in range(1, n_floors + 1)]
