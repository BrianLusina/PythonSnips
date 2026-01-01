from typing import List, Tuple, Set
from algorithms.graphs.number_of_islands.union_find import UnionFind


def num_of_islands(grid: List[List[str]]) -> int:
    islands = 0

    if len(grid) == 0 or not grid[0]:
        return islands

    visited: Set[Tuple[int, int]] = set()
    number_of_rows, number_of_cols = len(grid), len(grid[0])

    def dfs(start_r: int, start_c: int):
        stack = [(start_r, start_c)]

        while stack:
            r, c = stack.pop()

            if (
                r not in range(number_of_rows)
                or c not in range(number_of_cols)
                or grid[r][c] == "0"
                or (r, c) in visited
            ):
                continue

            visited.add((r, c))
            # [0, 1] -> move right along column
            # [0, -1] -> move left along column
            # [1, 0] -> move down along row
            # [-1, 0] -> move up along row
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in directions:
                stack.append((r + dr, c + dc))

    for row in range(number_of_rows):
        for col in range(number_of_cols):
            if grid[row][col] == "1" and (row, col) not in visited:
                islands += 1
                dfs(row, col)

    return islands


def num_islands_union_find(grid: List[List[str]]) -> int:
    if not grid:
        return 0

    cols = len(grid[0])
    rows = len(grid)
    uf = UnionFind(grid)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                grid[r][c] = "0"

                if r + 1 < rows and grid[r + 1][c] == "1":
                    uf.union(r * cols + c, (r + 1) * cols + c)
                if c + 1 < cols and grid[r][c + 1] == "1":
                    uf.union(r * cols + c, r * cols + c + 1)

    count = uf.get_count()
    return count
