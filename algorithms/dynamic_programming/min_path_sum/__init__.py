from typing import List


def min_path_sum_in_triangle(triangle: List[List[int]]) -> int:
    """
    Finds the minimum path sum in a given triangle of numbers
    This uses bottom up dynamic programming by starting at the bottom, we ensure that every decision made at a higher row
    is based on the perfect knowledge of the best possible paths below it

    Complexity:
    Time Complexity results in O(n^2), since we visit every number in the triangle exactly once. For n rows, there are
    roughtl n^2/2 elements.
    Space Complexity is O(1) since the triangle input array is updated in place

    Args:
        triangle(list): A list of lists of integers representing the triangle
    Returns:
        The minimum path sum in the triangle
    """
    row_count = len(triangle)

    # start from the second to last row, since the bottom row has no children to begin with
    for row in range(row_count - 2, -1, -1):
        # ensures that we visit every element for the current row
        for col in range(row + 1):
            # Each cell is updated to include the minimum path sum from the row below
            triangle[row][col] += min(
                triangle[row + 1][col], triangle[row + 1][col + 1]
            )

    # the result trickles to the apex
    return triangle[0][0]


def min_path_sum_in_triangle_2(triangle: List[List[int]]) -> int:
    """
    Finds the minimum path sum in a given triangle of numbers
    This uses bottom up dynamic programming by starting at the bottom, we ensure that every decision made at a higher row
    is based on the perfect knowledge of the best possible paths below it

    Complexity:
    Time Complexity results in O(n^2), since we visit every number in the triangle exactly once. For n rows, there are
    roughtl n^2/2 elements.
    Space Complexity is O(n) since the triangle input array's last row is copied over

    Args:
        triangle(list): A list of lists of integers representing the triangle
    Returns:
        The minimum path sum in the triangle
    """
    dp = triangle[-1][:]
    row_count = len(triangle)

    # start from the second to last row, since the bottom row has no children to begin with
    for row_idx in range(row_count - 2, -1, -1):
        # ensures that we visit every element for the current row
        for col_idx in range(row_idx + 1):
            # Each cell is updated to include the minimum path sum from the row below
            dp[col_idx] = triangle[row_idx][col_idx] + min(dp[col_idx], dp[col_idx + 1])

    # the result trickles to the apex
    return dp[0]


def min_path_sum_grid(grid: List[List[int]]) -> int:
    # m = number of rows, n = number of columns
    m = len(grid)
    n = len(grid[0])

    # Iterate over every cell in row-major order
    for i in range(m):
        for j in range(n):
            if i == 0 and j > 0:
               # First row but not [0][0]: we can only come from the left
                grid[i][j] += grid[i][j - 1]
            elif j == 0 and i > 0:
                # First column but not [0][0]: we can only come from above
                grid[i][j] += grid[i - 1][j]
            elif i > 0 and j > 0:
                 # For all other cells, choose the minimum of:
                # - the path sum from above (i-1, j)
                # - the path sum from the left (i, j-1)
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])

    # The bottom-right cell now contains the minimum path sum
    return grid[m - 1][n - 1]


def min_path_sum_grid_2(grid: List[List[int]]) -> int:
    if not grid or not grid[0]:
        return 0

    n_rows, n_cols = len(grid), len(grid[0])

    for i in range(1, n_rows):
        grid[i][0] += grid[i - 1][0]

    for i in range(1, n_cols):
        grid[0][i] += grid[0][i - 1]

    for r in range(1, n_rows):
        for c in range(1, n_cols):
            grid[r][c] += min(grid[r - 1][c], grid[r][c - 1])

    return grid[-1][-1]
