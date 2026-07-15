from typing import Dict, Tuple
from functools import lru_cache


def unique_paths_math(m: int, n: int) -> int:
    """Uses math formula"""
    ans = 1
    x = m + n - 2
    k = min(n - 1, m - 1)

    for i in range(1, k + 1):
        ans *= x
        x -= 1
        ans /= i

    return int(ans)


def unique_paths_top_down(m: int, n: int) -> int:
    """Uses top-down approach with memoization

    We are going to traverse all the unique paths, and store the values of the number of unique paths of each cell
    in our cache. Slight difference, we can start at m,n and traverse towards 0,0 to get the same result, which allows
    us to reuse the function as our recursive function.

    Complexity Analysis:
    - Time Complexity: O(m*n)
    - Space Complexity: O(m*n)
    """
    cache: Dict[Tuple[int, int], int] = {}

    @lru_cache(None)
    def unique_path_helper(row: int, col: int) -> int:
        # If already calculated, re-use those
        if (row, col) in cache:
            return cache[(row, col)]

        # if we reach 1 for either, that is the base case
        if row == 1 or col == 1:
            # set to 1
            result = 1
        else:
            # set the current value to bottom + right cell or in our case since we are starting from the bottom right,
            # set the current value to be the top + left cell
            result = unique_path_helper(row - 1, col) + unique_path_helper(row, col - 1)
        # cache result for later
        cache[(row, col)] = result
        return result

    return unique_path_helper(m, n)


def unique_paths_bottom_up(rows: int, cols: int) -> int:
    """Uses bottom-up approach

    Complexity Analysis

    Time Complexity: O(m * n) where m and n are the dimensions of the grid. For both the recursive and iterative
    solutions, we need to fill in a table of size m x n.

    Space Complexity: O(m * n) where m and n are the dimensions of the grid. The recursive solution uses O(m * n) space
    due to the call stack, while the iterative solution uses O(m * n) space for the dp table.
    """
    dp = [[0] * cols for _ in range(rows)]

    # Set base case: there is only one way to reach any cell in the first row (moving only right)
    for r in range(cols):
        dp[0][r] = 1

    # Set base case: there is only one way to reach any cell in the first column (moving only down)
    for r in range(rows):
        dp[r][0] = 1

    # Fill in the rest of the table
    for i in range(1, rows):
        for j in range(1, cols):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[rows - 1][cols - 1]
