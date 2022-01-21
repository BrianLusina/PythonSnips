from itertools import chain, islice
from typing import List


def matrix_reshape(mat: List[List[int]], r: int, c: int) -> List[List[int]]:
    """
    Reshapes a given matrix into a new one with a different size r x c keeping its original data
    @param mat: input matrix
    @param r: new row
    @param c: new column
    @return: reshaped matrix
    """
    if len(mat) * len(mat[0]) != r * c:
        return mat
    values = (val for row in mat for val in row)
    return [[next(values) for _ in range(c)] for _ in range(r)]


def matrix_reshape_2(mat: List[List[int]], r: int, c: int) -> List[List[int]]:
    """
    Reshapes a given matrix into a new one with a different size r x c keeping its original data
    @param mat: input matrix
    @param r: new row
    @param c: new column
    @return: reshaped matrix
    """
    flat = [val for row in mat for val in row]
    if len(flat) != r * c:
        return mat
    tuples = zip(*([iter(flat)] * c))
    return list(map(list, tuples))


def matrix_reshape_3(mat: List[List[int]], r: int, c: int) -> List[List[int]]:
    """
    Reshapes a given matrix into a new one with a different size r x c keeping its original data
    @param mat: input matrix
    @param r: new row
    @param c: new column
    @return: reshaped matrix
    """
    if len(mat) * len(mat[0]) != r * c:
        return mat

    it = chain(*mat)
    return [list(islice(it, c)) for _ in range(r)]
