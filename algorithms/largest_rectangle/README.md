Skyline Real Estate Developers is planning to demolish a number of old, unoccupied buildings and construct a shopping mall in their place. Your task is to find the largest solid area in which the mall can be constructed.

There are a number of buildings in a certain two-dimensional landscape. Each building has a height, given by

h[i] where i = [1, n]. If you join k adjacent buildings, they will form a solid rectangle of area
k * min(h[i]), h[i + 1], ..., h[i + k - 1])

Example:
h = [3,2,3]

A rectangle of height h = 2 and length k = 3 can be constructed within the boundaries. The area formed is: 
h * k = 2 * 3 = 6

Function Description

Complete the function largestRectangle int the editor below. It should return an integer representing the largest rectangle that can be formed within the bounds of consecutive buildings.

largestRectangle has the following parameter(s):

int h[n]: the building heights
Returns
- long: the area of the largest rectangle that can be formed within the bounds of consecutive buildings
