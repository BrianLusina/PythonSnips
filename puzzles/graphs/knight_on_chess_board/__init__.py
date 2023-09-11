from collections import deque
from dataclasses import dataclass


@dataclass
class Cell:
    x: int
    y: int
    distance: int


def is_inside(x, y, a, b):
    if 0 <= x < a and 0 <= y < b:
        return True
    return False


def knight(rows, cols, initial_x, initial_y, destination_x, destination_y) -> int:
    queue = deque()

    # possible moves for a knight
    dx = [2, 2, -2, -2, 1, 1, -1, -1]
    dy = [1, -1, 1, -1, 2, -2, 2, -2]

    source = Cell(x=initial_x - 1, y=initial_y - 1, distance=0)
    queue.append(source)

    # make all cells unvisited
    visited = [[False for _ in range(cols)]
               for _ in range(rows)]

    # initial position is visited
    visited[initial_x - 1][initial_y - 1] = True

    while queue:
        cell = queue.popleft()

        if cell.x == destination_x - 1 and cell.y == destination_y - 1:
            return cell.distance

        for i in range(8):
            x = cell.x + dx[i]
            y = cell.y + dy[i]

            if is_inside(x, y, rows, cols) and not visited[x][y]:
                visited[x][y] = True
                t = Cell(x=x, y=y, distance=cell.distance + 1)
                queue.append(t)

    return -1
