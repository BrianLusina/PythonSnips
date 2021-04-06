Description:

Magic squares are numbers in an n * n grids, where the sum of numbers sides and diagonals all give the same sum.

Example:

Below depicts the famous Lo Shu Magic Square. Where the sum of an array rows and columns, as well as diagonals, all sum
up to 15.

var arr = [
[8, 1, 6]
[3, 5, 7]
[4, 9, 2]
]; Notes:

Your aim is to create a magicSquare() function that returns a boolean, to match whether the n * n array is a magic
square, or not.

magicSquare([[8, 1, 6], [3, 5, 7], [4, 9, 2]]) // should return true magicSquare([[8, 6, 1], [3, 5, 7], [4, 9, 2]]) //
should return false magicSquare([[9, 14, 7],[8, 10, 12],[13, 6, 11]]) // should return true Arrays that contain zero
length should return false as it not a real magic square

Only 3x3 and 4x4 magic squares will tested here
