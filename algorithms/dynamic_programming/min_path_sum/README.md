# Min Path Sum in Triangle

Given an array, triangle, return the minimum path sum from top to bottom. You may move to an adjacent number in the row
below at each step. More formally, if you are at index i in the current row, you may move to either index i or index 
i+1 in the next row.

## Constraints

- 1 <= triangle.length <= 200
- triangle[0].length == 1
- triangle[i].length == triangle[i - 1].length + 1
- -10^4 <= triangle[i][j] <= 10^4

## Solution

The goal is to find the minimum path sum from the top of a triangular array to its base, moving at each step to one of 
the two adjacent numbers in the next row. A greedy choice at the top may fail because a small value early on can lead to
a costly region later, and plain recursion is inefficient since it revisits the same subproblems many times. This 
problem is a natural fit for dynamic programming:
the best path through a cell depends only on the best paths beneath it (optimal substructure), and many different routes
share the same suffixes (overlapping subproblems).

To solve it efficiently, we take a bottom-up approach. We begin with the last row, whose values represent the known 
final costs of any path ending there. From there, we move upward one row at a time. For each number, we determine its 
minimum path cost by adding its own value to the smaller of the two pre-calculated path costs in the row directly below 
it. This process effectively “folds” the triangle’s path information upward, continuously updating each row with the 
optimal costs from the level below. By this process’s peak, the single top number has been transformed to hold the total
of the most efficient path through the entire structure.

The following steps can be performed to implement the algorithm above:

1. First, we create a one-dimensional list, `dp`, to store our minimum path sums. This list is initialized as a copy of 
   the last row of the triangle, i.e., triangle[-1]. This serves as our base case, because the minimum path cost from 
   any number in the last row to the bottom is simply its own value.
2. Next, we iterate from the second-to-last row (rowIdx = len(triangle) - 2) of the triangle and move upward, one row at
   a time, until we reach the top (rowIdx = 0). This bottom-up order ensures that when we process a row, the optimal 
   path costs for the row below it are already calculated and stored in the dp list.
   - We create a nested loop inside the main loop that iterates through each number in the current row. 
     - For the current number, triangle[rowIdx][colIdx], we calculate its minimum path sum using:
       - min(dp[colIdx], dp[colIdx + 1])
       - After finding the minimum of the two, we add it to triangle[rowIdx][colIdx]. 
       - Finally, we update the dp list at the current position with this new, smaller total.

3. After the loops complete, the dp list contains the fully collapsed path information. The final answer for the entire 
   journey, from the top to the bottom, is now the list’s first element, dp[0].

### Time Complexity

The time complexity is O(n^2) where n is the number of rows in the triangle. This is because the algorithm processes
each element exactly once, and the total number of elements in a triangle with n rows is about n * (n + 1)/2, which 
grows quadratically.

### Space Complexity

The space complexity is O(n) since we only maintain a single working array `dp` with one entry per row.

--- 

## Min Path Sum in Grid

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum
of all numbers along its path.

> Note: You can only move either down or right at any point in time.

Example 1
```text
Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
```

Example 2:

```text
Input: grid = [[1,2,3],[4,5,6]]
Output: 12
```

### Constraints

- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 200
- 0 <= grid[i][j] <= 200

## Topics

- Array
- Dynamic Programming
- Matrix
