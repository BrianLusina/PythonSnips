from typing import List


def flood_fill(image: List[List[int]], sr: int, sc: int, new_color: int) -> List[List[int]]:
    starting_cell_color = image[sr][sc]

    if starting_cell_color == new_color:
        return image

    rows, cols = len(image), len(image[0])

    def dfs(r: int, c: int):
        if image[r][c] == starting_cell_color:
            image[r][c] = new_color
            # move up a row, i.e. move up vertically
            if r >= 1:
                dfs(r - 1, c)

            # move down a row, i.e. move down vertically
            if r + 1 < rows:
                dfs(r + 1, c)

            # move to the left, i.e. move left horizontally
            if c >= 1:
                dfs(r, c - 1)

            # move to the right, i.e. move right horizontally
            if c + 1 < cols:
                dfs(r, c + 1)

    dfs(sr, sc)
    return image
