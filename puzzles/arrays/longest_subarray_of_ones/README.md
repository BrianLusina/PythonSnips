# Longest Subarray of 1's After Deleting One Element

Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no
such subarray.

```plain
Example 1:

Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
Example 2:

Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's
is [1,1,1,1,1].
Example 3:

Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.
```

## Solution

### Approach: Sliding Window

#### Intuition

We have a binary array nums with size `N`; we need to delete exactly one element from it and then return the longest
subarray having only 1. Since we need to maximize the count of 1 in the subarray, we should not delete a 1, except in
the case when the array has all elements as 1 (then we don't have a choice).

Although we need a subarray with all elements as 1, we can afford to have one 0 as we can delete it. We will keep a
window and keep adding elements as long as the count of 0s in it doesn't exceed one. Once the number of 0s exceeds one,
we will shrink the window from the left side till the count of 0 comes under the limit; then, we can compare the size of
the current window with the longest subarray we have got so far.

This algorithm will cover the edge case with no zeroes, as in that case, the zeroCount will never exceed 1, and our
window will cover the whole array. In the end, the difference between the first and last index would provide the array
size minus 1, which is intended as we need to delete one element.

#### Algorithm

1. Initialize three variables:
    1. longestWindow to 0; this is the longest window having at most one 0 we have seen so far.
    2. left to 0; this is the left end of the window from where it starts.
    3. last_zero, this is the index of the last seen zero element

2. Iterate over the array, and keep track of the current element. If the element is zero, move the left pointer
   to `last_zero`+1 and set the `last_zero` to the pointer, in this case, it will be `right`

3. Update the variable longestWindow with the current window length, i.e. `right - left`. Note that this subtraction
   will give the number of elements in the window minus 1, as we need to delete one element too.

4. Return longestWindow.

#### Complexity Analysis

Here, `N` is the size of the array nums.

##### Time complexity: O(N)

Each element in the array will be iterated over twice at max. Each element will be iterated over for the first time in
the for loop; then, it might be possible to re-iterate while shrinking the window in the while loop. No element can be
iterated more than twice. Therefore, the total time complexity would equal O(N)O(N)O(N).

##### Space complexity: O(1)

Apart from the three variables, we don't need any extra space; hence the total space complexity is constant.

## Related Topics

- Array
- Dynamic Programming
- Sliding Window
