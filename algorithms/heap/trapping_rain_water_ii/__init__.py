from typing import List
import heapq


class Cell:
    """
    Class to store the height and coordinates of a cell in a grid
    """

    def __init__(self, height: int, row: int, col: int):
        self.height = height
        self.row = row
        self.col = col

    def __lt__(self, other: "Cell"):
        """Comparison method for the priority queue(min-heap)"""
        return self.height < other.height


def trap_rain_water(height_map: List[List[int]]) -> int:
    # Direction arrays that help us navigate the neighbors of a cell
    d_row = [0, 0, -1, 1]
    d_col = [-1, 1, 0, 0]

    # Number of rows and columns in the height map
    num_rows = len(height_map)
    num_cols = len(height_map[0])

    # Create a num_rows * num_cols boolean grid, called visited, with all its values initialized to False
    visited = [[False] * num_cols for _ in range(num_rows)]

    # Initialize a priority queue (min-heap) of Cells, called boundary. This will process cells in increasing height order
    boundary: List[Cell] = []

    # Add the first and last column cells to the boundary and mark them as visited
    # Add the first and last column cells to the boundary and mark them as visited
    for i in range(num_rows):
        heapq.heappush(boundary, Cell(height_map[i][0], i, 0))
        heapq.heappush(
            boundary,
            Cell(height_map[i][num_cols - 1], i, num_cols - 1),
        )
        visited[i][0] = visited[i][num_cols - 1] = True

    # Add the first and last row cells to the boundary and mark them as visited
    for i in range(num_cols):
        heapq.heappush(boundary, Cell(height_map[0][i], 0, i))
        heapq.heappush(
            boundary,
            Cell(height_map[num_rows - 1][i], num_rows - 1, i),
        )
        visited[0][i] = visited[num_rows - 1][i] = True

    # Initialize total water volume to 0
    total_water_volume = 0

    def is_cell_valid(row: int, col: int) -> bool:
        """
        Checks if a cell is within the bounds of the height map
        """
        return 0 <= row < num_rows and 0 <= col < num_cols

    # Process cells in the boundary (min-heap will always pop the smallest height)
    while boundary:
        # Pop the top cell from the boundary. This is the cell with the smallest height in the unexplored part of the
        # boundary
        current_cell = heapq.heappop(boundary)

        current_row = current_cell.row
        current_col = current_cell.col
        min_boundary_height = current_cell.height

        # Explore all 4 neighbors of the current cell
        for direction in range(4):
            # Calculate the row and column of the neighbor cell
            neighbor_row = current_row + d_row[direction]
            neighbor_col = current_col + d_col[direction]

            # Check if the neighbor cell is within the bounds of the height map and has not been visited
            if (
                is_cell_valid(neighbor_row, neighbor_col)
                and not visited[neighbor_row][neighbor_col]
            ):
                # Calculate the height of the neighbor cell
                neighbor_height = height_map[neighbor_row][neighbor_col]

                # If the neighbor's height is less than the current boundary height, water can be trapped
                if neighbor_height < min_boundary_height:
                    # Add the trapped water volume
                    water_volume = min_boundary_height - neighbor_height
                    total_water_volume += water_volume

                # Push the neighbor cell to the boundary with updated height(to prevent water leakage) and mark it as visited
                heapq.heappush(
                    boundary,
                    Cell(
                        max(neighbor_height, min_boundary_height),
                        neighbor_row,
                        neighbor_col,
                    ),
                )
                visited[neighbor_row][neighbor_col] = True

    # Return the total amount of trapped water
    return total_water_volume


def trap_rain_water_2(height_map: List[List[int]]) -> int:
    # Get dimensions of the height map
    m, n = len(height_map), len(height_map[0])

    # Edge case: if grid is too small to trap any water
    if m < 3 or n < 3:
        return 0

    # Min-heap to process cells by height (boundary cells first)
    min_heap = []
    # Track visited cells to avoid reprocessing
    visited = [[False] * n for _ in range(m)]

    # Push all boundary cells into the min-heap and mark them visited
    for r in range(m):
        for c in range(n):
            if r == 0 or r == m - 1 or c == 0 or c == n - 1:
                heapq.heappush(min_heap, (height_map[r][c], r, c))
                visited[r][c] = True

    # Directions for exploring neighbors (up, down, left, right)
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    total_water = 0

    # Process cells in order of increasing height
    while min_heap:
        # Pop the cell with the smallest height (current water boundary)
        height, row, col = heapq.heappop(min_heap)

        # Explore all 4 neighbors
        for dr, dc in directions:
            nr, nc = row + dr, col + dc

            # Skip out-of-bounds or already visited cells
            if nr < 0 or nr >= m or nc < 0 or nc >= n or visited[nr][nc]:
                continue

            # Water trapped at neighbor = max(0, current boundary height - neighbor height)
            total_water += max(0, height - height_map[nr][nc])

            # Push neighbor into heap with effective height (max of boundary or its own)
            heapq.heappush(min_heap, (max(height, height_map[nr][nc]), nr, nc))

            # Mark neighbor as visited
            visited[nr][nc] = True

    return total_water
