from typing import List, Deque, Tuple
from collections import deque


def oranges_rotting(grid: List[List[int]]) -> int:
    """Returns the minimum time it will take to make all oranges rotten in a grid. If this is not possible, -1 is returned

    Since we must track time, a breadth-first search approach makes the most sense, as we can track each iteration of
    our bfs loop, and update the time before moving on to the next.

    First, we need to iterate our grid looking for rotten oranges to add to our queue. Note, if we also take the time
    during this iteration to count the number of fresh oranges, we can save a little time in the end.

    Once we have a queue of oranges, we just need to run our BFS and update our time after we exhaust all current cells
    in each iteration of it, and finally return the time as long as we have successfully converted all fresh oranges to
    rotten ones.

    Time Complexity: O(m*n)
    where m is the number of rows, and n is the number of columns. We must traverse the graph once to find all our
    fresh/rotten oranges, and then potentially again during our BFS.

    Space Complexity: O(m*n). In the worst case, all oranges will be rotten, and our queue will be of size m*n.

    Args:
        grid (List): Grid of oranges.
    Returns:
        int: minimum number of minutes it will take to make all oranges rotten or -1 if not possible
    """
    rows, cols = len(grid), len(grid[0])
    # keep track of rotten oranges
    queue: Deque[Tuple[int, int]] = deque([])

    # number of fresh oranges
    fresh = 0

    # iterate the grid
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                fresh += 1

            # add grid position of rotten orange
            if grid[r][c] == 2:
                queue.append((r, c))

    # keep track of time
    time = 0
    # directions in the form of x,y
    directions = ((1, 0), (0, 1), (-1, 0), (0, -1))

    # while we have a queue of rotten oranges, and there are still fresh oranges.
    while queue and fresh > 0:
        for _ in range(len(queue)):
            row, col = queue.popleft()

            # check the 4 adjacent oranges of this rotten orange
            for dr, dc in directions:
                # position of adjacent orange
                r, c = row + dr, col + dc

                # check the adjacent orange is in bounds and fresh
                if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != 1:
                    continue

                # they are fresh, therefore, it becomes rotten
                grid[r][c] = 2
                fresh -= 1

                # add new rotten orange to the queue, we won't reach it on this iteration, as we are only iterating
                # through the rotten from the last iteration
                queue.append((r, c))

        # since we only looped through the rotten oranges inside the queue, and not the adjacent ones, we can increment
        # the time now, and on the next iteration we will check those adjacent ones
        time += 1

    # if we turned all oranges rotten, return the time, else -1
    return time if fresh == 0 else -1
