def tower_builder(n_floors):
    space = n_floors - 1
    m = []
    for i in range(1, n_floors * 2, 2):
        m.append(i * '{:^6}'.format('*'))
        space -= 1
    return m
