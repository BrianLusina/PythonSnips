from typing import List


def num_of_islands(grid: List[List[str]]) -> int:
    islands = 0

    if len(grid) == 0 or not grid[0]:
        return islands

    visited = set()
    number_of_rows, number_of_cols = len(grid), len(grid[0])

    def dfs(r: int, c: int):
        if r not in range(number_of_rows) or c not in range(number_of_cols) or grid[r][c] == "0" or (r, c) in visited:
            return

        visited.add((r, c))
        # [0, 1] -> move right along column
        # [0, -1] -> move left along column
        # [1, 0] -> move down along row
        # [-1, 0] -> move up along row
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        for dr, dc in directions:
            dfs(r + dr, c + dc)

    for row in range(number_of_rows):
        for col in range(number_of_cols):
            if grid[row][col] == "1" and (row, col) not in visited:
                islands += 1
                dfs(row, col)

    return islands
