from typing import List


def square_multiply(a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
    n_rows_a, n_cols_a = len(a), len(a[0])
    n_rows_b, n_cols_b = len(b), len(b[0])

    if n_rows_a != n_rows_b:
        return []

    if n_cols_a != n_cols_b:
        return []

    c = [[0] * n_cols_b for _ in range(n_rows_a)]

    for i in range(n_rows_a):
        for j in range(n_cols_b):
            row_sum = 0
            for k in range(n_rows_b):
                row_sum += a[i][k] * b[k][j]
            c[i][j] += row_sum

    return c
