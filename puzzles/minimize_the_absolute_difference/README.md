# Minimize the absolute difference

Given three sorted arrays A, B and Cof not necessarily same sizes.

Calculate the minimum absolute difference between the maximum and minimum number from the triplet a, b, c such that a,
b, c belongs arrays A, B, C respectively.

i.e. minimize | max(a,b,c) - min(a,b,c) |.

Example :

Input:

A : [ 1, 4, 5, 8, 10 ]
B : [ 6, 9, 15 ]
C : [ 2, 3, 6, 6 ]
Output:

1
Explanation: We get the minimum difference for a=5, b=6, c=6 as | max(a,b,c) - min(a,b,c) | = |6-5| = 1.

## Solution

Start with the largest elements in each of the arrays A, B & C. Maintain a variable to update the answer during each of
the steps to be followed.
In every step, the only possible way to decrease the difference is to decrease the maximum element out of the three
elements.
So traverse to the next largest element in the array containing the maximum element for this step and update the answer
variable.
Repeat this step until the array containing the maximum element ends. 