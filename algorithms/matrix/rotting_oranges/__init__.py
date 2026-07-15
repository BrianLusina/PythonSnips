from typing import List, Deque, Tuple
from collections import deque


def oranges_rotting(grid: List[List[int]]) -> int:
    if not grid:
        return 0

    # Grid dimensions
    rows, cols = len(grid), len(grid[0])

    # Count fresh oranges and collect initial rotten oranges
    fresh_count = 0
    queue: Deque[Tuple[int, int]] = deque()

    # Scan the grid to find all rotten oranges (value 2) and count fresh oranges (value 1)
    for row_idx in range(rows):
        for col_idx in range(cols):
            if grid[row_idx][col_idx] == 2:
                # Add rotten orange position to queue
                queue.append((row_idx, col_idx))
            elif grid[row_idx][col_idx] == 1:
                # Increment fresh oranges
                fresh_count += 1

    # Time elapsed in minutes
    minutes_elapsed = 0
    # Direction vectors for 4-directional movement (up, down, left, right)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # BFS to rot adjacent oranges
    while queue and fresh_count > 0:
        minutes_elapsed += 1

        # Process all oranges that rot in the current minute
        current_level_size = len(queue)
        for _ in range(current_level_size):
            current_row, current_col = queue.popleft()

            # Check all four adjacent cells
            for row_delta, col_delta in directions:
                next_row = current_row + row_delta
                next_col = current_col + col_delta

                # Check if the adjacent cell is within bounds and contains a fresh orange
                if (
                    0 <= next_row < rows
                    and 0 <= next_col < cols
                    and grid[next_row][next_col] == 1
                ):
                    # Rot the fresh orange
                    grid[next_row][next_col] = 2
                    queue.append((next_row, next_col))
                    fresh_count -= 1

                # Early termination if all oranges are rotten
                if fresh_count == 0:
                    return minutes_elapsed

    # Return -1 if there are still fresh oranges, otherwise return 0
    return -1 if fresh_count > 0 else 0
