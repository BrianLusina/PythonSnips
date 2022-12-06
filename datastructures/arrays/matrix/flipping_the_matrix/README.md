# Flipping the Matrix

Sean invented a game involving a 2nx2n matrix where each cell of the matrix contains an integer. He can reverse any of
its
rows or columns any number of times. The goal of the game is to maximize the sum of the elements in the nxn submatrix
located in the upper-left quadrant of the matrix.

Given the initial configurations for q matrices, help Sean reverse the rows and columns of each matrix in the best
possible way so that the sum of the elements in the matrix's upper-left quadrant is maximal.

Example:

matrix = [[1,2], [3,4]]

```
1 2
3 4
```

It is 2x2 and we want to maximize the top left quadrant, a 1x1 matrix. Reverse row 1:

```
1 2
4 3
```

and now reverse column 0:

```
4 2
1 3
```

The maximal sum is 4

Another example:

```
matrix = [[112, 42, 83, 119], [56, 125, 56, 49], [15, 78, 101, 43], [62, 98, 114, 108]]
maximal sum = 414
```

Explanation:

Start out with a 2nx2n matrix:

```
matrix = [
          [112, 42, 83, 119],
          [56, 125, 56, 49],
          [15, 78, 101, 43],
          [62, 98, 114, 108]
         ]
```

Perform following operations to maximize the sum of nxn sub matrix in upper left quadrant:

Reverse column 2 [83, 56,101, 114] -> [114,101,56,83], resulting in the matrix:

```
matrix = [
          [112, 42, 114, 119],
          [56, 125, 101, 49],
          [15, 78, 56, 43],
          [62, 98, 83, 108]
         ]
```

Reverse row 0 [1112,42,114,119] -> [119,114,42,112], resulting in matrix:

```
matrix = [
          [119, 114, 42, 112],
          [56, 125, 101, 49],
          [15, 78, 56, 43],
          [62, 98, 83, 108]
         ]
```

Sum of the values in the nxn submatrix in the upper left quadrant is `119+114+56+125=414`
