from typing import List
from math import factorial as fac


def binomial(x, y):
    try:
        return fac(x) // fac(y) // fac(x - y)
    except ValueError:
        return 0


def pascals_triangle(nth: int) -> List[List[int]]:
    """
    Generate Pascal's triangle of binomial coefficients upto the nth row
    :param nth: Nth row to generate Pascal's triangle
    :return: returns list of lists of each row or binomial coefficients of Pascal's triangle
    """
    result: List[List[int]] = []
    for x in range(nth + 1):
        result.append([binomial(x, y) for y in range(x + 1)])

    return result


def pascal_nth_row(nth: int) -> List[int]:
    """
    Gets Pascal's Triangle Nth row and returns it
    This is much faster than calculating the whole triangle and then fetching by its index.
    We instead use the formula:
        NCr = (NCr - 1 * (N - r + 1)) / r where 1 ≤ r ≤ N
        as the nth row consists of the following sequence:
        NC0, NC1, ......, NCN - 1, NCN
    """
    ncr_1 = 1
    row: List[int] = [ncr_1]

    for i in range(1, nth + 1):
        ncr = (ncr_1 * (nth - i + 1)) // i
        row.append(ncr)
        ncr_1 = ncr

    return row
