from typing import List


def search_matrix(matrix: List[List[int]], target: int) -> bool:
    """
    Search a 2D matrix for a target value. If the target value is found, return True, otherwise return False.
    Args:
        matrix (List[List[int]]): 2D matrix to search in.
        target (int): Target value to search for.
    Returns:
        bool: True if the target value is found in the matrix, False otherwise.
    """
    if not matrix:
        return False
    if not matrix[0]:
        return False

    n_rows = len(matrix)
    n_cols = len(matrix[0])

    left, right = 0, n_rows * n_cols - 1
    while left <= right:
        mid = (left + right) // 2
        row, col = mid // n_cols, mid % n_cols
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False


def search_matrix_2(matrix: List[List[int]], target: int) -> bool:
    """
    Search a 2D matrix for a target value. If the target value is found, return True, otherwise return False.
    Args:
        matrix (List[List[int]]): 2D matrix to search in.
        target (int): Target value to search for.
    Returns:
        bool: True if the target value is found in the matrix, False otherwise.
    """
    # Get dimensions of the matrix
    num_rows, num_cols = len(matrix), len(matrix[0])

    # Initialize binary search boundaries
    # Treat the 2D matrix as a flattened 1D array
    left, right = 0, num_rows * num_cols - 1
    first_true_index = -1

    # Binary search using the template: find first index where element >= target
    while left <= right:
        mid = (left + right) // 2

        # Convert 1D index to 2D coordinates
        row, col = divmod(mid, num_cols)

        # Feasible condition: matrix[row][col] >= target
        if matrix[row][col] >= target:
            first_true_index = mid
            right = mid - 1
        else:
            left = mid + 1

    # Check if first_true_index points to the target
    if first_true_index == -1:
        return False
    row, col = divmod(first_true_index, num_cols)
    return matrix[row][col] == target
