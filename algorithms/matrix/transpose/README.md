# Transpose

Take input text and output it transposed.

Given an input text output it transposed.

Roughly explained, the transpose of a matrix:

```
ABC
DEF
```

is given by:

```
AD
BE
CF
```

Rows become columns and columns become rows. See <https://en.wikipedia.org/wiki/Transpose>.

If the input has rows of different lengths, this is to be solved as follows:

- Pad to the left with spaces.
- Don't pad to the right.

Therefore, transposing this matrix:

```
ABC
DE
```

results in:

```
AD
BE
C
```

And transposing:

```
AB
DEF
```

results in:

```
AD
BE
 F
```

In general, all characters from the input should also be present in the transposed output. That means that if a column
in the input text contains only spaces on its bottom-most row(s), the corresponding output row should contain the spaces
in its right-most column(s).

## Source

Reddit r/dailyprogrammer challenge #270 [Easy]
. [https://www.reddit.com/r/dailyprogrammer/comments/4msu2x/challenge_270_easy_transpose_the_input_text](https://www.reddit.com/r/dailyprogrammer/comments/4msu2x/challenge_270_easy_transpose_the_input_text)


--

# Transpose Matrix

You're given a 2D array of integers <span>matrix</span>. Write a function that returns the transpose of the matrix.

The transpose of a matrix is a flipped version of the original matrix across its main diagonal (which runs from top-left
to bottom-right); it switches the row and column indices of the original matrix.

You can assume the input matrix always has at least 1 value; however its width and height are not necessarily the same.

## Examples

Example 1:

```text
Input:
matrix = [
    [1, 2],
]

Output:
[
    [1],
    [2]
]
```

Example 2:

```text
Input:
matrix = [
    [1, 2],
    [3, 4],
    [5, 6],
]

Output:
[
    [1, 3, 5],
    [2, 4, 6],
]
```

Example 3:

```text
Input:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

Output:
[
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9],
]
```

## Hints

- The row and column indices of each entry in the matrix should be flipped. For example, the value at `matrix[1][2]` will
  be at `matrix[2][1]` in the transpose of the matrix.
- Each column in the matrix should be become a row in the transpose of the matrix. Each row in the matrix should become 
  a column in the transpose of the matrix.
- Try iterating one column at a time, and with each column, create a row of the values to add to the transpose of the
  matrix.

## Solution

The transpose of a matrix `A` with dimensions `R x C` is a matrix `ans` with dimensions C x R for which `ans[c][r]` = `A[r][c]`.

Let's initialize a new matrix ans representing the answer. Then, we'll copy each entry of the matrix as appropriate.

### Complexity Analysis

#### Time Complexity: O(R*C)

Where `R` and `C` are the number of rows and columns in the given matrix `A`.

#### Space Complexity: O(R*C)

The space used by the answer.

