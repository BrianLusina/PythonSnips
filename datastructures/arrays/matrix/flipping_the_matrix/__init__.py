from typing import List


def flipping_matrix(matrix: List[List[int]]) -> int:
    n = len(matrix)
    total = 0
    for i in range(n // 2):
        for j in range(n // 2):
            total += max(matrix[i][j], matrix[i][n - j - 1], matrix[n - i - 1][j], matrix[n - i - 1][n - j - 1])

    return total
