from typing import List


def transpose(input_lines: str) -> str:
    """
    transposes letters in input lines like a matrix, where the columns become rows and rows
    become columns
    :param input_lines: lines to transpose
    :return: String with the characters transposed
    """
    lines = input_lines.split("\n")
    zipped = map(list, [line.ljust(len(max(lines, key=len))) for line in lines])

    return "\n".join("".join(line) for line in zip(*zipped)).strip()


def transpose_matrix(matrix: List[List[int]]) -> List[List[int]]:
    """
    transposes a matrix by making the columns the rows and the rows the columns
    Args:
        matrix: matrix to transpose
    Returns:
        Transposed matrix
    """
    if not matrix:
        return []

    n_rows = len(matrix)
    n_cols = len(matrix[0])

    transposed_matrix = [[0] * n_rows for _ in range(n_cols)]

    for row in range(n_rows):
        for col in range(n_cols):
            value = matrix[row][col]
            transposed_matrix[col][row] = value

    return transposed_matrix
