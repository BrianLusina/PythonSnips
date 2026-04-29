from typing import List, Tuple, Set


def max_area_of_island(grid: List[List[int]]) -> int:
    """
    Given a non-empty 2D array grid of 0s and 1s, an island is a group of 1s
    connected 4-directionally (horizontal or vertical.) You may assume all 4
    edges of the grid are surrounded by water.
    this returns the maximum area of an island in the grid
    Args:
        grid(list): 2D array grid of 0s and 1s
    Returns:
        int: max area of island
    """
    num_rows, num_cols = len(grid), len(grid[0])
    max_area = 0

    visited: Set[Tuple[int, int]] = set()

    def area(row: int, col: int) -> int:
        if not (
            0 <= row < num_rows
            and 0 <= col < num_cols
            and (row, col) not in visited
            and grid[row][col]
        ):
            return 0

        visited.add((row, col))
        return (
            1
            + area(row + 1, col)
            + area(row - 1, col)
            + area(row, col - 1)
            + area(row, col + 1)
        )

    for r in range(num_rows):
        for c in range(num_cols):
            max_area = max(max_area, area(r, c))

    return max_area


def max_area_of_island_iterative(grid: List[List[int]]) -> int:
    """
    Given a non-empty 2D array grid of 0s and 1s, an island is a group of 1s
    connected 4-directionally (horizontal or vertical.) You may assume all 4
    edges of the grid are surrounded by water.
    this returns the maximum area of an island in the grid
    Args:
        grid(list): 2D array grid of 0s and 1s
    Returns:
        int: max area of island
    """
    num_rows, num_cols = len(grid), len(grid[0])
    max_area = 0

    visited: Set[Tuple[int, int]] = set()

    for row_idx, row in enumerate(grid):
        for col_idx, val in enumerate(row):
            if val and (row_idx, col_idx) not in visited:
                shape = 0
                stack = [(row_idx, col_idx)]
                visited.add((row_idx, col_idx))

                while stack:
                    r, c = stack.pop()
                    shape += 1
                    for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                        if (
                            0 <= nr < num_rows
                            and 0 <= nc < num_cols
                            and grid[nr][nc]
                            and (nr, nc) not in visited
                        ):
                            stack.append((nr, nc))
                            visited.add((nr, nc))
                max_area = max(max_area, shape)

    return max_area
