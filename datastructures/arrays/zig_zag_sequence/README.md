# Zig Zag Sequence

Given an array of n distinct integers, transform the array into a zig zag sequence by permuting the array elements. A
sequence will be called a zig zag sequence if the first k elements in the sequence are in increasing order and the last
k elements are in decreasing order, where k = (n+1)/2. You need to find the lexicographically smallest zig zag sequence
of the given
array.

Example 1:

a = [2,3,5,1,4]
Now if we permute the array as [1,2,5,3,4], the result is a zig zag sequence.

Example 2:
a = [7, 2, 5, 4, 3, 6, 1]
expected = [1, 2, 3, 7, 6, 5, 4]
