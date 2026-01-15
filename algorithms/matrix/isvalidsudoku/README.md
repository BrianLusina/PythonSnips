# Valid Sudoku

Given a 9 × 9 Sudoku board, determine whether it is valid. A board is considered valid if all of the following conditions
hold (considering only the filled cells):

- Each row contains the digits 1–9 at most once. 
- Each column contains the digits 1–9 at most once. 
- Each of the nine 3 × 3 sub-boxes contains the digits 1–9 at most once.

You do not need to check whether the Sudoku is solvable; only whether the current filled entries obey these rules.

> Note:A partially filled Sudoku board can be valid even if it is not necessarily solvable. You only need to verify that
> the filled cells adhere to the given rules.

## Constraints

- `board.length` == 9
- `board[i].length` == 9
- `board[i][j]` is a digit or a `.`

## Examples

![Example 1](images/examples/is_valid_sudoku_example_1.png)
![Example 2](images/examples/is_valid_sudoku_example_2.png)
![Example 3](images/examples/is_valid_sudoku_example_3.png)

## Solution

The intuition behind this solution is simple: instead of trying to solve the Sudoku or perform any form of search or
backtracking, we treat the board as a constraint-checking problem. As we scan the board once, cell by cell, we ensure
that every filled digit obeys the Sudoku rules, which require no repetition in its row, column, or 3×3 sub-box. To do
this efficiently, we maintain three arrays of hash sets:

- row_sets[9]: Tracks digits seen in each row.
- col_sets[9]: Tracks digits seen in each column.
- box_sets[9]: Tracks digits seen in each 3×3 sub-box.

Each set keeps track of the digits that have already appeared in that specific region. For every filled cell, if the
digit is already in its row, column, or sub-box set, then we’ve detected a rule violation, and the board is invalid. If
we finish scanning all 81 cells without encountering duplicates, the board is valid. This transforms the problem into a
clean, single-pass constraint check, eliminating the need for any kind of search or backtracking.

Using the intuition above, we implement the algorithm as follows:
- Initialize an empty array, `row_sets`, to track digits in each row.
- Initialize an empty array, `col_sets`, to track digits in each column. 
- Initialize an empty array, `box_sets`, to track digits in each 3×3 sub-box. 
- Use an outer loop to iterate through rows.
  - Use an inner loop to iterate through columns.
  - Retrieve the value present at the current rows and columns of the board: `cell = board[r][c].`
    - If `cell` is a .,
      - Skip this value
    - Compute the index of the 3×3 sub-box that contains the current cell using: `(r // 3) * 3 + (c // 3)`.
    - Check whether `cell` is already present in the corresponding row, column, or box set.
      - If it is, return False
    - If no duplicate is found, we insert `cell` into:
      - `row_set[r]`, 
      - `col_set[c]`, 
      - `box_set[box_idx]`.
- If all cells are processed without conflicts, return TRUE, indicating that the given Sudoku board is valid.

![Example 1](images/solutions/is_valid_sudoku_solution_1.png)
![Example 2](images/solutions/is_valid_sudoku_solution_2.png)
![Example 3](images/solutions/is_valid_sudoku_solution_3.png)
![Example 4](images/solutions/is_valid_sudoku_solution_4.png)
![Example 5](images/solutions/is_valid_sudoku_solution_5.png)
![Example 6](images/solutions/is_valid_sudoku_solution_6.png)
![Example 7](images/solutions/is_valid_sudoku_solution_7.png)
![Example 8](images/solutions/is_valid_sudoku_solution_8.png)
![Example 9](images/solutions/is_valid_sudoku_solution_9.png)
![Example 10](images/solutions/is_valid_sudoku_solution_10.png)
![Example 11](images/solutions/is_valid_sudoku_solution_11.png)
![Example 12](images/solutions/is_valid_sudoku_solution_12.png)

### Complexity

#### Time

The time complexity of this algorithm is constant, O(1).

Although we iterate through all 81 cells of a 9×9 Sudoku board, the board size is fixed. In each cell, we perform
constant-time operations:

- Hash set lookups
- Hash set insertions 
- Simple arithmetic for computing the box index

As 81 operations are a fixed constant, the overall runtime is O(1) in terms of theoretical complexity.

#### Space

The space complexity of this algorithm is constant, O(1). This is because we create:

- 9 row sets 
- 9 column sets 
- 9 box sets

Each can contain at most 9 digits, so a constant amount of memory bounds the total storage.

Total extra space = 27 sets * max 9 values = 243, which is a constant number. So, the space complexity is O(1).
