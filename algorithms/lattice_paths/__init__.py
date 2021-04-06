"""
Lattice paths, this gets the number of routes ina given grid lattice
"""
from functools import reduce


# lattice_paths = lambda n: reduce(lambda x, y: x * y, range(1, n + 1), 1)


def lattice_paths(grid):
    """

    :param grid:
    :return:
    """
    return reduce(lambda x, y: x * y, range(1, grid + 1), 1)


if __name__ == "__main__":
    n, m = 20, 20
    print("Routes through a", n, "x", m, "grid", lattice_paths(n + m) // lattice_paths(n) // lattice_paths(m))
