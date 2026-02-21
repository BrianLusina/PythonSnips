from typing import List


def min_total_distance(grid):
    rows, cols = [], []

    # Helper function to calculate total distance to the median
    def get_min_distance(points: List[int]) -> int:
        distance = 0
        i, j = 0, len(points) - 1

        # Use two pointers to accumulate distance from both ends toward the center
        while i < j:
            distance += points[j] - points[i]
            i += 1
            j -= 1

        return distance

    # Collect all row indices where grid[i][j] == 1
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                rows.append(i)

    # Collect all column indices where grid[i][j] == 1
    for j in range(len(grid[0])):
        for i in range(len(grid)):
            if grid[i][j] == 1:
                cols.append(j)

    # Compute total vertical and horizontal distances to medians
    return get_min_distance(rows) + get_min_distance(cols)


def min_total_distance_2(grid: List[List[int]]) -> int:
    """
    Find the minimum total distance for all people to meet at one point.
    The optimal meeting point is the median of all x-coordinates and y-coordinates.

    Args:
        grid: 2D grid where 1 represents a person's location, 0 represents empty space

    Returns:
        Minimum total Manhattan distance for all people to meet
    """

    def calculate_distance_sum(positions: List[int], meeting_point: int) -> int:
        """
        Calculate sum of distances from all positions to the meeting point.

        Args:
            positions: List of coordinate values (either row or column indices)
            meeting_point: The target coordinate to measure distance to

        Returns:
            Sum of absolute distances
        """
        return sum(abs(position - meeting_point) for position in positions)

    # Collect all row and column indices where people are located
    row_indices = []
    column_indices = []

    for row_index, row in enumerate(grid):
        for column_index, cell_value in enumerate(row):
            if cell_value == 1:  # Person found at this location
                row_indices.append(row_index)
                column_indices.append(column_index)

    # Sort column indices to find median (row indices already sorted due to iteration order)
    column_indices.sort()

    # Find median positions (optimal meeting point)
    # Using bit shift for integer division by 2
    median_row = row_indices[len(row_indices) >> 1]
    median_column = column_indices[len(column_indices) >> 1]

    # Calculate total distance as sum of row distances and column distances
    total_distance = calculate_distance_sum(
        row_indices, median_row
    ) + calculate_distance_sum(column_indices, median_column)

    return total_distance
