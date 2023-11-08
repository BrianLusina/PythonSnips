from typing import Dict, Tuple


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


def unique_paths_bottom_up(m: int, n: int) -> int:
    """Uses bottom-up approach

    Complexity Analysis:
    - Time Complexity: O(m*n)
    - Space Complexity: O(n)
    """
    row = [1] * n

    # go through all rows except the last one
    for i in range(m - 1):
        new_row = [1] * n

        # go through every column except the right most column
        # because the last value in every row is 1
        # start at second to last position and
        # keep going until we get to the beginning (reverse order)

        for j in range(n - 2, -1, -1):
            # right value + value below
            new_row[j] = new_row[j + 1] + row[j]
        # update the row
        row = new_row

    return row[0]
