from typing import List


def min_path_sum(triangle: List[List[int]]) -> int:
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


def min_path_sum_2(triangle: List[List[int]]) -> int:
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
