from typing import List


def max_area_of_island(grid: List[List[int]]) -> int:
    """
    Given a non-empty 2D array grid of 0s and 1s, an island is a group of 1s
    connected 4-directionally (horizontal or vertical.) You may assume all 4
    edges of the grid are surrounded by water.
    this returns the maximum area of an island in the grid
    """
    num_rows, num_cols = len(grid), len(grid[0])
    max_area = 0

    visited = set()

    def area(row: int, col: int) -> int:
        if not (0 <= row < num_rows and 0 <= col < num_cols and (row, col) not in visited and grid[row][col]):
            return 0

        visited.add((row, col))
        return 1 + area(row + 1, col) + area(row - 1, col) + area(row, col - 1) + area(row, col + 1)

    for r in range(num_rows):
        for c in range(num_cols):
            max_area = max(max_area, area(r, c))

    return max_area


def dfs(grid: List[List[int]], row: int, col: int) -> int:
    visited = set()

    if not (0 <= row < len(grid) and 0 <= col < len(grid[0])) and (row, col) not in visited and grid[row][col]:
        return 0

    visited.add((row, col))
    return 1 + dfs(grid, row + 1, col) + dfs(grid, row - 1, col) + dfs(grid, row, col + 1) + dfs(grid, row, col - 1)
