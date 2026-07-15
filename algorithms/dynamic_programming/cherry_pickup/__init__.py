from typing import List, Optional
from math import inf


def cherry_pickup_dp_top_down(grid: List[List[int]]) -> int:
    n = len(grid)
    memo = [[[None] * n for _ in range(n)] for _ in range(n)]

    def dp(r1: int, c1: int, c2: int) -> Optional[int | float]:
        r2 = r1 + c1 - c2
        if (
            n == r1
            or n == r2
            or n == c1
            or n == c2
            or grid[r1][c1] == -1
            or grid[r2][c2] == -1
        ):
            return -inf
        elif r1 == c1 == n - 1:
            return grid[r1][c1]
        elif memo[r1][c1][c2] is not None:
            return memo[r1][c1][c2]
        else:
            result = grid[r1][c1] + (c1 != c2) * grid[r2][c2]
            result += max(
                dp(r1, c1 + 1, c2 + 1),
                dp(r1 + 1, c1, c2 + 1),
                dp(r1, c1 + 1, c2),
                dp(r1 + 1, c1, c2),
            )
        memo[r1][c1][c2] = result
        return result

    return max(0, dp(0, 0, 0))


def cherry_pickup_dp_top_down_2(grid: List[List[int]]) -> int:
    n = len(grid)

    # dp[k][i1][i2] represents the maximum cherries collected when:
    # - Person 1 is at position (i1, j1) where j1 = k - i1
    # - Person 2 is at position (i2, j2) where j2 = k - i2
    # - k represents the sum of coordinates (i + j), indicating the step number
    dp = [[[-inf] * n for _ in range(n)] for _ in range(2 * n - 1)]

    # Initialize starting position - both persons start at (0, 0)
    dp[0][0][0] = grid[0][0]

    # Iterate through each step (k represents Manhattan distance from origin)
    for k in range(1, 2 * n - 1):
        for row1 in range(n):
            for row2 in range(n):
                # Calculate column positions based on current step and row
                col1 = k - row1
                col2 = k - row2

                # Check if positions are valid and not blocked by thorns
                if (
                    not 0 <= col1 < n
                    or not 0 <= col2 < n
                    or grid[row1][col1] == -1
                    or grid[row2][col2] == -1
                ):
                    continue

                # Calculate cherries to pick at current positions
                cherries_picked = grid[row1][col1]
                # Avoid double counting if both persons are at the same cell
                if row1 != row2:
                    cherries_picked += grid[row2][col2]

                # Check all possible previous positions for both persons
                # Each person could have come from either up or left
                for prev_row1 in range(row1 - 1, row1 + 1):
                    for prev_row2 in range(row2 - 1, row2 + 1):
                        # Ensure previous positions are within bounds
                        if prev_row1 >= 0 and prev_row2 >= 0:
                            dp[k][row1][row2] = max(
                                dp[k][row1][row2],
                                dp[k - 1][prev_row1][prev_row2] + cherries_picked,
                            )

    # Return the maximum cherries collected, or 0 if no valid path exists
    return max(0, dp[-1][-1][-1])


def cherry_pickup_dp_bottom_up(grid: List[List[int]]) -> int:
    n = len(grid)
    dp = [[-inf] * n for _ in range(n)]
    dp[0][0] = grid[0][0]

    for t in range(1, 2 * n - 1):
        dp2 = [[-inf] * n for _ in range(n)]
        for i in range(max(0, t - (n - 1)), min(n - 1, t) + 1):
            for j in range(max(0, t - (n - 1)), min(n - 1, t) + 1):
                if grid[i][t - i] == -1 or grid[j][t - j] == -1:
                    continue
                val = grid[i][t - i]
                if i != j:
                    val += grid[j][t - j]
                dp2[i][j] = max(
                    dp[pi][pj] + val
                    for pi in (i - 1, i)
                    for pj in (j - 1, j)
                    if pi >= 0 and pj >= 0
                )
        dp = dp2
    return max(0, dp[n - 1][n - 1])
