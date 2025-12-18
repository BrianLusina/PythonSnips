from typing import List
from itertools import permutations


def minimum_moves(grid: List[List[int]]) -> int:
    """
    This function finds the minimum number of moves required to place exactly one stone in each grid cell.

    Args:
        grid(list): 2D grid of integers of size (3 × 3), where each value represents the number of stones in the given
        cell
    Returns:
        int: minimum number of moves required to place exactly one stone in each grid cell
    """
    # stores every stone beyond the first one in a cell, this becomes the source
    surplus_list = []
    # for every cell with 0 stones, this contains the coordinates of that cell. this becomes the target
    empty_list = []

    minimum_number_of_moves = float("inf")

    # iterate through the grid and add the cell that has surplus stones multiple times to the surplus list, for example,
    # if cell grid[1][1] has 3 stones, add it twice to the surplus list
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 0:
                empty_list.append([row, col])
            elif grid[row][col] > 1:
                count = grid[row][col]
                for c in range(count - 1):
                    surplus_list.append([row, col])

    # iterate through every possible permutation of the sources, trying every possible assignment to the targets
    for perms in permutations(surplus_list):
        # calculate the total number of moves for this permutation
        total_moves = 0
        for i in range(len(perms)):
            total_moves += abs(perms[i][0] - empty_list[i][0]) + abs(perms[i][1] - empty_list[i][1])
        # return the minimum number of moves
        minimum_number_of_moves = min(minimum_number_of_moves, total_moves)

    return minimum_number_of_moves
