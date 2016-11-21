def tower_builder(n_floors):
    tower = []
    n_space = n_floors - 1
    for _ in range(1, n_floors + 1):
        floor = ("\n" * (n_space - 1)) + ("*" * n_floors) + ("\n" * (n_space - 1))
        n_floors += 2
        n_space -= 1
        tower.append(floor)
        if len(tower) == n_floors:
            break
    return tower
