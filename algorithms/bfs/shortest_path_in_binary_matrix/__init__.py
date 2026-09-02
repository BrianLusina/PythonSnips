from typing import List
from collections import deque


def shortest_path_binary_matrix(grid: List[List[int]]) -> int:
    n = len(grid)

    # Check if starting cell is blocked
    if n == 0 or grid[0][0] == 1:
        return -1

    # Mark starting cell as visited
    grid[0][0] = 1
    # Path length starts at 1
    result = 1
    # Initialize BFS queue with starting position
    queue = deque([(0, 0)])

    is_within_bounds = lambda r, c: 0 <= r < n and 0 <= c < n

    # BFS find the shortest path
    while queue:
        # Process all cells at current level
        level_size = len(queue)
        for _ in range(level_size):
            row, col = queue.popleft()

            # Check if we've reached the end
            if row == n - 1 and col == n - 1:
                return result

            # Explore all 8 directions from the current cell
            for next_row in range(row - 1, row + 2):
                for next_col in range(col - 1, col + 2):
                    # Check if cell is within bounds and unvisited
                    if (
                        is_within_bounds(next_row, next_col)
                        and grid[next_row][next_col] == 0
                    ):
                        # Mark cell as visited
                        grid[next_row][next_col] = 1
                        # Add cell to queue for further exploration
                        queue.append((next_row, next_col))
        # Increment path length
        result += 1

    return -1


def shortest_path_binary_matrix_2(grid: List[List[int]]) -> int:
    # Get grid size
    n = len(grid)

    # If start or end is blocked, no path exists
    if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
        return -1

    # If single cell grid and it's clear
    if n == 1:
        return 1

    # All 8 directions (including diagonals)
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    is_within_bounds = lambda r, c: 0 <= r < n and 0 <= c < n

    # BFS queue holds (row, col, distance)
    bfs_queue = deque()
    bfs_queue.append((0, 0, 1))

    # Mark start as visited by setting it to 1
    grid[0][0] = 1

    # Standard BFS for shortest path in unweighted graph
    while bfs_queue:
        row, col, dist = bfs_queue.popleft()

        # Explore neighbors
        for dr, dc in directions:
            new_row = row + dr
            new_col = col + dc

            # Check bounds and if cell is clear (0)
            if is_within_bounds(new_row, new_col) and grid[new_row][new_col] == 0:
                # If we reached the end, return path length
                if new_row == n - 1 and new_col == n - 1:
                    return dist + 1

                # Mark visited and push to queue
                grid[new_row][new_col] = 1
                bfs_queue.append((new_row, new_col, dist + 1))

    # No path found
    return -1
