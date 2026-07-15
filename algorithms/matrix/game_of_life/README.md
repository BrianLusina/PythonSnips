# Game of Life

According to [Wikipedia's article](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life): "The Game of Life, also known
simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead
(represented by a 0). Each cell interacts with its [eight neighbors](https://en.wikipedia.org/wiki/Moore_neighborhood)
(horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

- Any live cell with fewer than two live neighbors dies as if caused by under-population.
- Any live cell with two or three live neighbors lives on to the next generation.
- Any live cell with more than three live neighbors dies, as if by over-population.
- Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

The next state of the board is determined by applying the above rules simultaneously to every cell in the current state of the m x n grid board. In this process, births and deaths occur simultaneously.

Given the current state of the board, update the board to reflect its next state.

Note that you do not need to return anything.

## Examples

Example 1:

```text
Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
```

Example 2:

```text
Input: board = [[1,1],[1,0]]
Output: [[1,1],[1,1]]
```

## Constraints

- m == board.length
- n == board[i].length
- 1 <= m, n <= 25
- `board[i][j]` is 0 or 1.

Follow up:

- Could you solve it in-place? Remember that the board needs to be updated simultaneously: You cannot update some cells
  first and then use their updated values to update other cells.
- In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause
  problems when the active area encroaches upon the border of the array (i.e., live cells reach the border). How would
  you address these problems?

## Topics

- Array
- Matrix
- Simulation

## Solution

The core intuition is to update all cells simultaneously without corrupting neighbor counts. We encode transitions in
place: 1 means alive (and may stay alive), -1 means was alive and will die (underpopulation/overpopulation), 0 means
dead (and may stay dead), and 2 means was dead and will become alive (reproduction). While counting neighbors, we only
care about the original state, so we test abs(`board[r][c]) == 1`. This is true for 1 and -1 (originally alive) and false
for 0 and 2 (originally dead). With that, we finish a full pass marking transitions, then a quick second pass to normalize
to 0 or 1.

Using the intuition above, we implement the algorithm as follows:

1. Store the board’s dimensions in rows and cols.
2. Define an array neighbors = {-1, 0, 1}. The Cartesian product {−1,0,1} × {−1,0,1} gives the relative offsets to all
   eight neighboring cells around a given cell. We skip the (0, 0) pair as it represents the cell itself. This allows us
   to systematically check every neighbor’s state when counting alive cells.
3. Iterate over every cell (row, col) in the grid. For each cell:
   - Initialize a counter liveNeighbors = 0.
   - To count alive neighbors, loop i = 0..2 and j = 0..2 to form a relative offset (neighbors[i], neighbors[j]):
     - Compute the neighbor’s coordinates: r = row + neighbors[i] and c = col + neighbors[j].
     - If (r, c) is in bounds and abs(``board[r][c]) == 1`` (originally alive), increment liveNeighbors.
   - After counting liveNeighbors, apply the Game of Life rules using the cell’s original state (the current value before
     any normalization):
     - If `board[row][col] == 1` and liveNeighbors is less than 2 (underpopulation) or greater than 3 (overpopulation),
       mark it as -1 to encode alive → dead.
     - Otherwise, if `board[row][col] == 0` and liveNeighbors is 3, mark it as 2 to encode dead → alive (reproduction).
     - Otherwise, leave the cell unchanged (1 stays 1, 0 stays 0).
4. Iterate through the board again to finalize the next generation by normalizing each cell back to 0 or 1:
   - If `board[row][col]` > 0 (values 1 or 2), set it to 1.
   - Otherwise (for values 0 or -1), set it to 0.
5. The normalized board now represents the next state after applying the rules simultaneously.


### Time complexity

The time complexity is O(m×n), where m and n are the dimensions of the board. Each cell inspects up to 8 neighbors
(constant work) and is processed twice (marking, then normalization).

### Space complexity

The algorithm’s space complexity is constant, O(1).
