from typing import List


def flood_fill(image: List[List[int]], sr: int, sc: int, new_color: int) -> List[List[int]]:
    """
    We perform the algorithm by painting the starting pixels, plus adjacent pixels of the same color, and so on.
    Say 'color' is the color of the starting pixel. Let's floodfill the starting pixel: we change the color of that
    pixel to the new color, then check the 4 neighboring pixels to make sure they are valid pixels of the same color,
    and of the valid ones, we floodfill those, and so on. We can use a function dfs to perform a floodfill on a target
    pixel.

    Complexity Analysis:
    Time Complexity: O(N), where NN is the number of pixels in the image. We might process every pixel.
    Space Complexity: O(N), the size of the implicit call stack when calling dfs.
    @param image: image grid to flood fill
    @param sr: starting row position
    @param sc: starting column position
    @param new_color: new color
    @return: new image grid flood filled with new colors
    """
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
