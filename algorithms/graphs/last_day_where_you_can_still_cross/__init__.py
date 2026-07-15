from typing import List, Tuple
from datastructures.sets.union_find import UnionFind


def latest_day_to_cross_binary_search(
    row: int, col: int, cells: List[List[int]]
) -> int:
    # Binary search for first day where crossing becomes impossible
    left, right = 1, len(cells)
    # tracks the first day where crossing becomes impossible
    first_true_index = -1

    cardinal_directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Checks to see if a given row and column is within the grid bounds
    is_within_bounds = lambda r, c: 0 <= r < row and 0 <= c < col

    def can_cross(day: int) -> bool:
        """Check if it is possible to cross from top to bottom on the given day"""
        # Build the grid state: Create a 2D grid, mark the first k cells as water (1).
        grid = [[0] * col for _ in range(row)]

        for i in range(day):
            r, c = cells[i]
            grid[r - 1][c - 1] = 1

        # BFS from top row: Initialize queue with all land cells from row 0.
        queue: List[Tuple[int, int]] = []
        for j in range(col):
            if grid[0][j] == 0:
                queue.append((0, j))
                grid[0][j] = 1

        # BFS exploration: For each cell, check if we've reached the bottom row. Explore all 4 directions, adding
        # unvisited land cells to the queue.
        idx = 0
        while idx < len(queue):
            x, y = queue[idx]
            idx += 1

            # Return True if we reach the bottom row, False otherwise.
            if x == row - 1:
                return True

            for dx, dy in cardinal_directions:
                next_x, next_y = x + dx, y + dy
                if is_within_bounds(next_x, next_y) and grid[next_x][next_y] == 0:
                    queue.append((next_x, next_y))
                    grid[next_x][next_y] = 1
        return False

    def feasible(day: int) -> bool:
        """Returns true when crossing is Not Possible."""
        return not can_cross(day)

    # Binary search loop
    while left <= right:
        mid = (left + right) // 2

        if feasible(mid):
            first_true_index = mid
            right = mid - 1
        else:
            left = mid + 1

    return first_true_index - 1


def last_day_to_cross_union_find(rows: int, cols: int, water_cells):
    # create a variable to keep track of the number of days
    day = 0
    # create the matrix that needs to be crossed
    matrix = [[0 for _ in range(cols)] for _ in range(rows)]
    # create the two virtual nodes, one before the first column and the other after the last column of the matrix
    left_node, right_node = 0, rows * cols + 1

    # specify the directions where water can move
    water_directions = [
        (1, 0),
        (0, 1),
        (-1, 0),
        (0, -1),
        (1, 1),
        (1, -1),
        (-1, 1),
        (-1, -1),
    ]

    # convert the water_cells from 1-based to 0-based array for the convenience
    water_cells = [(r - 1, c - 1) for r, c in water_cells]

    # initialize the UnionFind object, this will create the disjoint set union datastructure, an array - parents
    uf = UnionFind(rows * cols + 2)

    def find_index(current_row, current_col):
        """maps the index of the element in 2-D matrix to an index of the 1-D array (parents)"""
        return current_row * cols + (current_col + 1)

    def within_bounds(r, c):
        """checks whether the water cells to be connected are within the bounds of the matrix as per given dimensions"""
        if not (0 <= c < cols):
            return False
        if not (0 <= r < rows):
            return False
        return True

    # On each day, one cell of the matrix will get flooded
    for row, col in water_cells:
        # change the matrix's cell from land (0) to water (1)
        matrix[row][col] = 1

        # check if the recently flooded cell connects with any of the existing water cells
        for dr, dc in water_directions:
            if within_bounds(row + dr, col + dc) and matrix[row + dr][col + dc] == 1:
                uf.union(find_index(row, col), find_index((row + dr), (col + dc)))
        if col == 0:
            uf.union(find_index(row, col), left_node)
        if col == cols - 1:
            uf.union(find_index(row, col), right_node)

        # check if got a series of connected water cells from the left to the right side of the matrix
        if uf.find(left_node) == uf.find(right_node):
            break
        day += 1

    return day
