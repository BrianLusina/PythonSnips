def tower_builder(n_floors):
    return [("*" * (i * 2 - 1)).center(n_floors * 2 - 1)
            for i in range(1, n_floors + 1)]
