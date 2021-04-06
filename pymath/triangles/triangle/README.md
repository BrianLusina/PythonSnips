# Triangle

Write a program that can tell you if a triangle is equilateral, isosceles, or scalene and also be able to calculate the
area of the triangle and its perimeter

You are required to create 3 methods `kind`, `area` and `perimeter`

`kind` should return the kind of triangle either `equilateral`, `scalene` or `isosceles`

``` python
>>> Triangle(10, 10, 10).kind()
equilateral

>>> Triangle(3, 4, 4).kind()
isosceles

>>> Triangle(3, 4, 5).kind()
scalene
```

`area` should return the area of the triangle

``` python
>>> Triangle(3, 3, 3).area()
4
```

`perimeter` should return the perimeter of the triangle

``` python
>>> Triangle(2, 2, 2).perimeter()
6
```

## Notes:

1. round your result when calculating the area of the triangle to the nearest whole number
2. The program should raise an error if the triangle cannot exist.

## Hint

The triangle inequality theorem states:
z ≤ x + y where x,y, and z are the lengths of the sides of a triangle. In other words, the sum of the lengths of any two
sides of a triangle always exceeds or is equal to the length of the third side.

A corollary to the triangle inequality theorem is there are two classes of triangles--degenerate and non-degenerate. If
the sum of the lengths of any two sides of a triangle is greater than the length of the third side, that triangle is two
dimensional, has area, and belongs to the non-degenerate class. In mathematics, a degenerate case is a limiting case in
which an element of a class of objects is qualitatively different from the rest of the class and hence belongs to
another, usually simpler, class. The degenerate case of the triangle inequality theorem is when the sum of the lengths
of any two sides of a triangle is equal to the length of the third side. A triangle with such qualities is qualitatively
different from all the triangles in the non-degenerate class since it is one dimensional, looks like a straight line,
and has no area. Such triangles are called degenerate triangles and they belong to the degenerate class.

## Source

The Ruby Koans triangle project, parts 1 & 2 [http://rubykoans.com](http://rubykoans.com)

