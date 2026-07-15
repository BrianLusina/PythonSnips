from typing import List, Tuple, Set, DefaultDict
from collections import defaultdict
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


def num_of_distinct_islands(grid: List[List[int]]) -> int:
    """
    Returns the number of distinct islands.
    Args:
        grid (List[List[int]]): grid represented as a 2D list where 1 represents land and 0 represents water.
    Returns:
        int: number of distinct islands.
    """
    if not grid:
        return 0

    num_rows = len(grid)
    num_cols = len(grid[0])
    path: List[str] = []
    unique_islands: Set[str] = set()

    # A compact way to represent 4 directions
    # next_dir=1: up (dx=-1, dy=0)
    # next_dir=2: right (dx=0, dy=1)
    # next_dir=3: down (dx=1, dy=0)
    # next_dir=4: left (dx=0, dy=-1)
    dirs: Tuple[int, int, int, int, int] = (-1, 0, 1, 0, -1)

    def dfs(row: int, col: int, direction: int):
        """
        DFS approach to explore cells
        Args:
            row(int): row index
            col(int): column index
            direction(int): direction index taken to reach this cell(0 for starting pont, 1-4 for up/right/down/left
        """
        grid[row][col] = 0  # mark as visited
        # record the direction we came from
        path.append(str(direction))

        for next_dir in range(1, 5):
            next_row, next_col = row + dirs[next_dir - 1], col + dirs[next_dir]
            if (
                0 <= next_row < num_rows
                and 0 <= next_col < num_cols
                and grid[next_row][next_col] == 1
            ):
                dfs(next_row, next_col, next_dir)

        # Record backtracking (negative direction) to distinguish different shapes
        path.append(str(-direction))

    # We iterate through each cell in the grid
    for row_idx, row in enumerate(grid):
        for col_idx, cell in enumerate(row):
            # Found a new island, cell with a value of 1
            if cell:
                # when we find land, we star ta DFS from that cell to explore the entire land
                dfs(row_idx, col_idx, 0)
                unique_islands.add("".join(path))
                path.clear()

    return len(unique_islands)


def num_of_distinct_islands_2(grid: List[List[int]]) -> int:
    # Initialize a set to keep track of visited cells
    visited: Set[Tuple[int, int]] = set()
    # Use defaultdict to count the distinct island shapes
    unique_islands: DefaultDict[Tuple[int, int], int] = defaultdict(int)

    def dfs(row, col, row_origin, column_origin, path: List[Tuple[int, int]]):
        nonlocal unique_islands
        nonlocal visited
        # Base case: out of bounds or already visited or water
        if (
            row < 0
            or col < 0
            or row >= len(grid)
            or col >= len(grid[0])
            or (row, col) in visited
            or grid[row][col] == 0
        ):
            return

        # Mark the current cell as visited
        visited.add((row, col))
        # Record the relative position of this cell from the origin of this island
        path.append((row - row_origin, col - column_origin))

        # Explore 4-directionally (up, down, left, right)
        dfs(row + 1, col, row_origin, column_origin, path)
        dfs(row - 1, col, row_origin, column_origin, path)
        dfs(row, col + 1, row_origin, column_origin, path)
        dfs(row, col - 1, row_origin, column_origin, path)

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            # Start DFS if it's a land cell and not yet visited
            if grid[row][col] == 1 and (row, col) not in visited:
                path: List[Tuple[int, int]] = []
                dfs(row, col, row, col, path)
                unique_islands[tuple(path)] += 1

    return len(unique_islands)
