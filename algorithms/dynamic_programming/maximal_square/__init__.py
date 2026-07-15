from typing import List


def maximal_square(matrix: List[List[int]]) -> int:
    """
    Returns the maximum area of a square containing only 1s in the 2D matrix
    Args:
        matrix(list): 2D matrix with 0s and 1s
    Returns:
        int: largest area of square with only 1s
    """
    if not matrix:
        return 0

    rows = len(matrix)
    cols = len(matrix[0])
    dp = [[0] * (cols + 1) for _ in range(rows + 1)]
    max_side = 0

    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            if matrix[i - 1][j - 1] == 1:
                top = dp[i - 1][j]
                left = dp[i][j - 1]
                diag = dp[i - 1][j - 1]
                dp[i][j] = min(top, left, diag) + 1
                max_side = max(max_side, dp[i][j])

    return max_side * max_side
