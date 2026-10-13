# Search a 2D Matrix

Given a two dimensional integer array matrix with m rows and n columns, determine whether the integer target exists in
matrix. Return true if target is present, otherwise return false.

The array matrix is sorted such that each row is in nondecreasing order, and the first element of each row is greater
than the last element of the previous row.

## Constraints

- m == matrix.length
- n == matrix[i].length
- 1 <= m,n <= 100
- -10^4 <= matrix[i][j], target <= 10^4

---
# Search a 2D Matrix II

Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.

## Examples

Example 1

```text
Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
Output: true
```

Example 2

```text
Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
Output: false
```

## Constraints

- m == matrix.length
- n == matrix[i].length
- 1 <= n, m <= 300
- -10^9 <= matrix[i][j] <= 10^9
- All the integers in each row are sorted in ascending order.
- All the integers in each column are sorted in ascending order.
- -10^9 <= target <= 10^9

## Topics

- Array
- Binary Search
- Divide and Conquer
- Matrix
