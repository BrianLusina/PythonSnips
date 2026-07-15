from typing import List


def maximal_rectangle(matrix: List[List[int]]) -> int:
    if not matrix:
        return 0

    rows = len(matrix)
    cols = len(matrix[0])

    # These arrays track the evolving histogram across rows:
    # height[j]     → height of stacked '1's at column j
    # left[j]       → furthest left boundary where current rectangle can extend
    # right[j]      → furthest right boundary where current rectangle can extend
    left = [0] * cols
    right = [cols] * cols
    height = [0] * cols

    max_area = 0

    for i in range(rows):
        current_left = 0  # dynamic left boundary for the current row
        current_right = cols  # dynamic right boundary for the current row

        # First forward pass: update heights and left boundaries
        for j in range(cols):
            if matrix[i][j] == 1:
                height[j] += 1  # grow histogram bar
                left[j] = max(
                    left[j], current_left
                )  # left[j] shrinks only when we encounter a 0
            else:
                height[j] = 0  # reset the bar height
                left[j] = 0  # reset left boundary
                current_left = j + 1  # next valid left candidate starts here

        # second backward pass: update right boundaries and compute areas
        for j in range(cols - 1, -1, -1):
            if matrix[i][j] == 1:
                right[j] = min(
                    right[j], current_right
                )  # right[j] shrinks whenever we hit a 0
            else:
                right[j] = cols  # reset boundary
                current_right = j  # next valid right candidate starts here

            # area of maximal rectangle using column j as part of the row floor
            max_area = max(max_area, (right[j] - left[j]) * height[j])

    return max_area


def maximal_rectangle_2(matrix: List[List[int]]) -> int:
    """
    Returns the maximum rectangle of a grid containing only 1s in the 2D matrix
    Args:
        matrix(list): 2D matrix with 0s and 1s
    Returns:
        int: largest area of rectangle with only 1s
    """
    if not matrix:
        return 0

    cols = len(matrix[0])
    heights = [0] * cols
    max_area = 0

    for row in matrix:
        for col_idx, col_value in enumerate(row):
            if col_value == 1:
                heights[col_idx] += 1
            else:
                heights[col_idx] = 0
        max_area = max(max_area, largest_rectangle_area(heights))

    return max_area


def largest_rectangle_area(heights: List[int]) -> int:
    """
    Find the largest rectangle area in a histogram.

    Uses monotonic stack to find the nearest smaller element on both left and right
    for each bar, then calculates the maximum rectangle area.

    Args:
        heights: List of bar heights in the histogram

    Returns:
        Area of the largest rectangle in the histogram
    """
    n = len(heights)
    if n == 0:
        return 0

    # Arrays to store indices of nearest smaller elements
    left_boundaries = [-1] * n  # Index of nearest smaller element on the left
    right_boundaries = [n] * n  # Index of nearest smaller element on the right

    # Find left boundaries using monotonic increasing stack
    stack = []
    for i, height in enumerate(heights):
        # Pop elements >= current height
        while stack and heights[stack[-1]] >= height:
            stack.pop()

        # If stack not empty, top element is the nearest smaller on left
        if stack:
            left_boundaries[i] = stack[-1]

        stack.append(i)

    # Find right boundaries using monotonic increasing stack (traverse right to left)
    stack = []
    for i in range(n - 1, -1, -1):
        height = heights[i]

        # Pop elements >= current height
        while stack and heights[stack[-1]] >= height:
            stack.pop()

        # If stack not empty, top element is the nearest smaller on right
        if stack:
            right_boundaries[i] = stack[-1]

        stack.append(i)

    # Calculate maximum rectangle area
    # For each bar, the rectangle extends from (left_boundary + 1) to (right_boundary - 1)
    max_area = max(
        height * (right_boundaries[i] - left_boundaries[i] - 1)
        for i, height in enumerate(heights)
    )

    return max_area
