# The Peak of a Mountain Array

A mountain array is defined as an array that

has at least 3 elements
has an element with the largest value called "peak", with index k. The array elements strictly increase from the first
element to A[k], and then strictly decreases from A[k + 1] to the last element of the array. Thus creating a "mountain"
of numbers.
That is, given A[0]<...<A[k-1]<A[k]>A[k+1]>...>A[n-1], we need to find the index k. Note that the peak element is
neither the first nor the last element of the array.

Find the index of the peak element. Assume there is only one peak element.

Input: 0 1 2 3 2 1 0

Output: 3

Explanation: the largest element is 3 and its index is 3.

## Related Topics

- Array
- Binary Search
