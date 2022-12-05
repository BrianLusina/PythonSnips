from typing import List


def diagonal_difference(matrix: List[List[int]]) -> int:
    left_to_right_sum = sum([matrix[x][x] for x in range(len(matrix))])
    right_to_left_sum = sum([matrix[x][len(matrix) - 1 - x] for x in range(len(matrix))])

    return abs(left_to_right_sum - right_to_left_sum)
