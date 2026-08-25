from typing import List
from collections import Counter, defaultdict


def count_black_blocks(m: int, n: int, coordinates: List[List[int]]) -> List[int]:
    # Dictionary to count black cells in each 2X2 block
    # Key: (top_left_row, top_left_col) of the 2x2 block
    # Value: number of black cells in the block
    block_black_count = Counter()
    # Check the 4 possible 2x2 blocks that could contain this cell.
    # The Offsets represent: current cell as top-left, top-right, bottom-left, bottom-right
    offsets = [(0, 0), (0, -1), (-1, -1), (-1, 0)]
    is_within_grid = lambda r, c: 0 <= r < m - 1 and 0 <= c < n - 1

    # For each black cell, update all 2x2 blocks that contain it
    for row, col in coordinates:
        for row_offset, col_offset in offsets:
            # Calculate the top-left corner of the potential 2x2 block
            block_row = row + row_offset
            block_col = col + col_offset

            # Check if this is 2x2 block is valid (within grid boundaries)
            if is_within_grid(block_row, block_col):
                block_black_count[(block_row, block_col)] += 1

    # Initialize result array for blocks with 0, 1,2,3,4 black cells
    result = [0] * 5

    # Count blocks by number of black cells they contain
    for black_cell_count in block_black_count.values():
        result[black_cell_count] += 1

    # Calculate blocks with 0 black cells
    # Total 2x2 blocks minus blocks that have at least one black cell
    total_blocks = (m - 1) * (n - 1)
    blocks_with_black_cells = len(block_black_count)
    result[0] = total_blocks - blocks_with_black_cells

    return result


def count_black_blocks_2(m: int, n: int, coordinates: List[List[int]]) -> List[int]:
    # Map each 2x2 block's top-left cell to how many black cells it contains
    block_count_map = defaultdict(int)

    # For each black cell, it can contribute to up to 4 neighboring 2x2 blocks
    for r, c in coordinates:
        # Enumerate possible top-left rows for blocks containing (r, c)
        for top_r in (r - 1, r):
            if 0 <= top_r < m - 1:
                # Enumerate possible top-left cols for blocks containing (r, c)
                for top_c in (c - 1, c):
                    if 0 <= top_c < n - 1:
                        # Increment black count for this 2x2 block
                        block_count_map[(top_r, top_c)] += 1

    # Total number of 2x2 blocks in the grid
    total_blocks = (m - 1) * (n - 1)

    # ans[k] = number of blocks with exactly k black cells
    ans = [0, 0, 0, 0, 0]

    # Count blocks that have at least 1 black cell using the hashmap
    for black_cells_in_block in block_count_map.values():
        ans[black_cells_in_block] += 1

    # Remaining blocks have 0 black cells
    ans[0] = total_blocks - sum(ans[1:])

    return ans
