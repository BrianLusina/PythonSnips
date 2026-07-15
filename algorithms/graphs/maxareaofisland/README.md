# Max Area of Island

You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (
horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

## Examples

Example 1:

![max_area_island](maxarea-grid.jpg)

```text
Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0]
,[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0]
,[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.
```

Example 2:
```text
Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0
```

## Solution

1. [Depth-First Search (Recursive)](#depth-first-search-recursive)
2. [Depth-First Search (Iterative)](#depth-first-search-iterative)

### Depth-First Search (Recursive)

We want to know the area of each connected shape in the grid, then take the maximum of these.

If we are on a land square and explore every square connected to it 4-directionally (and recursively squares connected
to those squares, and so on), then the total number of squares explored will be the area of that connected shape.

To ensure we don't count squares in a shape more than once, let's use `visited` to keep track of squares we haven't
visited before. It will also prevent us from counting the same shape more than once.

#### Complexity Analysis

##### Time Complexity

`O(R*C)`, where R is the number of rows in the given grid, and C is the number of columns. We visit every square once.

##### Space Complexity

`O(R*C)`, the space used by seen to keep track of visited squares and the space used by the call stack during our
recursion.

### Depth-First Search (Iterative)

We can try the same approach using a stack-based, (or "iterative") depth-first search.

Here, `visited` will represent squares that have either been visited or are added to our list of squares to visit (`stack`).
For every starting land square that hasn't been visited, we will explore 4-directionally around it, adding land squares
that haven't been added to `visited` to our stack.

On the side, we'll keep a count `shape` of the total number of squares seen during the exploration of this shape. We'll
want the running max of these counts.

#### Complexity Analysis

##### Time Complexity

`O(R*C)`, where R is the number of rows in the given grid, and C is the number of columns. We visit every square once.

##### Space Complexity

`O(R*C)`, the space used by seen to keep track of visited squares and the space used by stack

