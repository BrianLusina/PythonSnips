# Domino & Tromino Tiling

You have two types of tiles: a 2 x 1 domino shape and a tromino shape. You may rotate these shapes.

![Domino & Tromino](./domino_tromino_tiles.png)

Given an integer n, return the number of ways to tile an 2 x n board. Since the answer may be very large, return it
modulo 109 + 7.

In a tiling, every square must be covered by a tile. Two tilings are different if and only if there are two
4-directionally adjacent cells on the board such that exactly one of the tilings has both squares occupied by a tile.

Example 1:

![Domino & Tromino Tiling Example 1](./example_1_domino_tromino_tiling.png)

Input: n = 3
Output: 5
Explanation: The five different ways are show above.

Example 2:

Input: n = 1
Output: 1

## Related Topics

- Dynamic Programming
