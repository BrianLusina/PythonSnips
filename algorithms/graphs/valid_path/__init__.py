import math
from typing import List
from collections import deque


def valid_path(
    x: int,
    y: int,
    number_of_circles: int,
    radius_of_each_circle: int,
    x_coordinates: List[int],
    y_coordinates: List[int],
) -> bool:
    centers = list(zip(x_coordinates, y_coordinates))
    visited = [[0 for _ in range(y + 1)] for _ in range(x + 1)]

    def out_of_circles(tx, ty):
        nonlocal centers
        for center in centers:
            x_coord = center[0]
            y_coord = center[1]

            if (
                pow(tx - x_coord, 2) + pow(ty - y_coord, 2)
                <= radius_of_each_circle * radius_of_each_circle
            ):
                return False
        return True

    def is_safe(tx, ty):
        return 0 <= tx <= x and 0 <= ty <= y and out_of_circles(tx, ty)

    # Initialize the queue which holds the discovered cells whose neighbors  are not discovered yet.
    queue = deque()
    visited[0][0] = True
    queue.append((0, 0))

    directions = {(-1, 0), (1, 0), (0, 1), (0, -1), (-1, 1), (1, 1), (-1, -1), (1, -1)}

    while queue:
        cell = queue.popleft()
        cell_x_coordinate = cell[0]
        cell_y_coordinate = cell[1]

        if cell_x_coordinate == x and cell_y_coordinate == y:
            return True

        for direction in directions:
            ax = cell_x_coordinate + direction[0]
            ay = cell_y_coordinate + direction[1]

            if is_safe(ax, ay) and not visited[ax][ay]:
                visited[ax][ay] = True
                queue.append((ax, ay))

    return False
