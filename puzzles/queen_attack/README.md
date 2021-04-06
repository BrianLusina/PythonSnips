# Queen Attack

Write a program that positions two queens on a chess board and indicates whether or not they are positioned so that they
can attack each other.

In the game of chess, a queen can attack pieces which are on the same row, column, or diagonal.

A chessboard can be represented by an 8 by 8 array.

So if you're told the white queen is at (2, 3) and the black queen at
(5, 6), then you'd know you've got a set-up like so:

```plain
_ _ _ _ _ _ _ _
_ _ _ _ _ _ _ _
_ _ _ W _ _ _ _
_ _ _ _ _ _ _ _
_ _ _ _ _ _ _ _
_ _ _ _ _ _ B _
_ _ _ _ _ _ _ _
_ _ _ _ _ _ _ _
```

You'd also be able to answer whether the queens can attack each other. In this case, that answer would be yes, they can,
because both pieces share a diagonal.

You are required to write 2 functions `board` and `can_attack`. Both will take 2 parameters(tuples in Python). 1st tuple
will be the position of the white queen on the board and the second will be the position of the black queen on the
board.

`board` function should return a drawn out board with the position of both the white and black queen.

``` python
>>> board((2, 3), (5, 6)):
['________',
 '________',
 '___W____',
 '________',
 '________',
 '______B_',
 '________',
 '________']
```

> Note that this uses 0-based counting, so counting begins from 0

`can_attack` should check if either of the queens can attack each other from their positions.

``` python
>>> can_attack((2, 6), (5, 3))
True
```

If either `board` or `can_attack` are called with an invalid board position they should raise a ValueError with a
meaningful error message.

``` python
>>> board((0, 0), (7, 8))
ValueError
```

## Source

J Dalbey's Programming Practice
problems [http://users.csc.calpoly.edu/~jdalbey/103/Projects/ProgrammingPractice.html](http://users.csc.calpoly.edu/~jdalbey/103/Projects/ProgrammingPractice.html)
