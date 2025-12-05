# Number of Islands

Given an m x n 2D binary grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
If any '1' cells are connected to each other horizontally or vertically (not diagonally), they form an island
You may assume all four edges of the grid are all surrounded by water.

Constraints

- 1 <= `grid.length` <= 50
- 1 <= `grid[i].length` <= 50
- `grid[i][j]` is either '0' or '1'

## Examples

Example 1:

Input: grid = [
["1","1","1","1","0"],
["1","1","0","1","0"],
["1","1","0","0","0"],
["0","0","0","0","0"]
]
Output: 1

Example 2:

Input: grid = [
["1","1","0","0","0"],
["1","1","0","0","0"],
["0","0","1","0","0"],
["0","0","0","1","1"]
]
Output: 3
