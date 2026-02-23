from typing import List
import heapq
from collections import deque
import sys


def min_cost_dp(grid: List[List[int]]) -> int:
    if not grid:
        return 0

    num_rows = len(grid)
    num_cols = len(grid[0])

    min_changes = [[float("inf")] * num_cols for _ in range(num_rows)]
    min_changes[0][0] = 0

    while True:
        # Store previous state to check for convergence
        prev_state = [row[:] for row in min_changes]

        # forward pass: check cells coming from left and top
        for row in range(num_rows):
            for col in range(num_cols):
                # check cell above
                if row > 0:
                    min_changes[row][col] = min(
                        min_changes[row][col],
                        min_changes[row - 1][col]
                        + (0 if grid[row - 1][col] == 3 else 1),
                    )

                # check cell to the left
                if col > 0:
                    min_changes[row][col] = min(
                        min_changes[row][col],
                        min_changes[row][col - 1]
                        + (0 if grid[row][col - 1] == 1 else 1),
                    )

        # backward pass: check cells coming from right and bottom
        for row in range(num_rows - 1, -1, -1):
            for col in range(num_cols - 1, -1, -1):
                # check cell below
                if row < num_rows - 1:
                    min_changes[row][col] = min(
                        min_changes[row][col],
                        min_changes[row + 1][col]
                        + (0 if grid[row + 1][col] == 4 else 1),
                    )

                # Check cell to the right
                if col < num_cols - 1:
                    min_changes[row][col] = min(
                        min_changes[row][col],
                        min_changes[row][col + 1]
                        + (0 if grid[row][col + 1] == 2 else 1),
                    )

        # if not changes were made in this operation, we've found optimal solution
        if min_changes == prev_state:
            break

    return min_changes[num_rows - 1][num_cols - 1]


def min_cost_dijkstra(grid: List[List[int]]) -> int:
    if not grid:
        return 0

    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    num_rows = len(grid)
    num_cols = len(grid[0])

    # Min-heap ordered by cost. Each element is (cost, row, col)
    # Using list as heap, elements are tuples
    pq = [(0, 0, 0)]

    cost_grid = [[float("inf")] * num_cols for _ in range(num_rows)]
    cost_grid[0][0] = 0

    while pq:
        cost, row, col = heapq.heappop(pq)

        # skip if we've found a better path to this cell
        if cost_grid[row][col] != cost:
            continue

        # Try all 4 directions
        for d, (dr, dc) in enumerate(dirs):
            new_row = row + dr
            new_col = col + dc

            # Check if new position is valid
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
                # add cost = 1 if we need to change direction
                new_cost = cost + (d != (grid[row][col] - 1))

                # update if we found a better path
                if cost_grid[new_row][new_col] > new_cost:
                    cost_grid[new_row][new_col] = new_cost
                    heapq.heappush(pq, (new_cost, new_row, new_col))

    return cost_grid[num_rows - 1][num_cols - 1]


def min_cost_0_1_bfs(grid: List[List[int]]) -> int:
    if not grid:
        return 0
    num_rows = len(grid)
    num_cols = len(grid[0])
    # Direction vectors: right, left, down, up (matching grid values 1,2,3,4)
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    cost_grid = [[float("inf")] * num_cols for _ in range(num_rows)]
    cost_grid[0][0] = 0

    # Use deque for 0-1 BFS - add zero cost moves to front, cost=1 to back
    queue = deque([(0, 0)])

    # Check if coordinates are within grid bounds
    def is_valid(row: int, col: int) -> bool:
        return 0 <= row < num_rows and 0 <= col < num_cols

    while queue:
        row, col = queue.popleft()
        # Try all four directions
        for dir_idx, (dx, dy) in enumerate(dirs):
            new_row, new_col = row + dx, col + dy
            cost = 0 if grid[row][col] == dir_idx + 1 else 1

            # If position is valid and we found a better path
            if (
                is_valid(new_row, new_col)
                and cost_grid[row][col] + cost < cost_grid[new_row][new_col]
            ):
                cost_grid[new_row][new_col] = cost_grid[row][col] + cost

                # Add to back if cost=1, front if cost=0
                if cost == 1:
                    queue.append((new_row, new_col))
                else:
                    queue.appendleft((new_row, new_col))

    return cost_grid[num_rows - 1][num_cols - 1]


def min_cost_0_1_bfs_2(grid: List[List[int]]) -> int:
    if not grid:
        return 0
    # Store the number of rows and columns of grid
    num_rows, num_cols = len(grid), len(grid[0])

    # Create a 2D array of size num_rows x num_cols, initializing all cells to the maximum integer value
    cost_grid = [[sys.maxsize] * num_cols for _ in range(num_rows)]

    # Helper function to check if the new cell is valid and its cost can be improved
    def is_valid_and_improvable(row, col) -> bool:
        return (
            0 <= row < len(cost_grid)
            and 0 <= col < len(cost_grid[0])
            and cost_grid[row][col] != 0
        )

    # Create a deque and push the starting cell (0, 0) to the front
    dq = deque()
    dq.appendleft((0, 0))

    # Set its cost in cost_grid to 0
    cost_grid[0][0] = 0

    # Define an array representing the four possible movement directions
    dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    # Enter a loop that continues as long as the deque is not empty
    while dq:
        # Pop the front cell from the deque and store its coordinates in row and col
        row, col = dq.popleft()

        # Loop through each of the four directions in dirs
        for d in range(4):
            # Compute the coordinates of the adjacent cell
            new_row = row + dirs[d][0]
            new_col = col + dirs[d][1]

            # Check if the new cell is valid and its cost can be improved
            if is_valid_and_improvable(new_row, new_col):
                # Calculate the movement cost
                cost = 1 if grid[row][col] != (d + 1) else 0

                # Check whether the new cost is less than the current cost at the adjacent cell
                if cost_grid[row][col] + cost < cost_grid[new_row][new_col]:
                    # Update the cost of the adjacent cell
                    cost_grid[new_row][new_col] = cost_grid[row][col] + cost

                    if cost == 1:
                        # Push the new cell to the back
                        dq.append((new_row, new_col))
                    else:
                        # Push the new cell to the front
                        dq.appendleft((new_row, new_col))

    # Return the minimum cost stored at the bottom-right cell
    return cost_grid[num_rows - 1][num_cols - 1]


def min_cost_dfs_and_bfs(grid: List[List[int]]) -> int:
    # Direction vectors: right, left, down, up (matching grid values 1,2,3,4)
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    num_rows = len(grid)
    num_cols = len(grid[0])
    cost = 0

    # Track minimum cost to reach each cell
    cost_grid = [[float("inf")] * num_cols for _ in range(num_rows)]

    queue = deque()

    # DFS to explore all reachable cells with current cost
    def dfs(
        row: int,
        col: int,
        cost: int,
    ) -> None:
        if not is_unvisited(row, col):
            return

        cost_grid[row][col] = cost
        queue.append((row, col))

        # Follow the arrow direction without cost increase
        next_dir = grid[row][col] - 1
        dx, dy = dirs[next_dir]
        dfs(row + dx, col + dy, cost)

    # Check if cell is within bounds and unvisited
    def is_unvisited(row: int, col: int) -> bool:
        return (
            0 <= row < len(cost_grid)
            and 0 <= col < len(cost_grid[0])
            and cost_grid[row][col] == float("inf")
        )

    dfs(0, 0, cost)

    # BFS part - process cells level by level with increasing cost
    while queue:
        cost += 1
        level_size = len(queue)

        for _ in range(level_size):
            row, col = queue.popleft()

            # Try all 4 directions for next level
            for dir_idx, (dx, dy) in enumerate(dirs):
                dfs(row + dx, col + dy, cost)

    return cost_grid[num_rows - 1][num_cols - 1]
