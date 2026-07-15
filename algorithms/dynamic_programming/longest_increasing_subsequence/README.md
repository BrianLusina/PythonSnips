# Longest Increasing Subsequence

Find the longest increasing subsequence of a given array of integers, A.

In other words, find a subsequence of array in which the subsequence's elements are in strictly increasing order, and in
which the subsequence is as long as possible.

In this case, return the length of the longest increasing subsequence.

```plain
Input 1:

A = [1, 2, 1, 5]
Output = 3
The longest increasing subsequence: [1, 2, 5]

Input 2:

A = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
Output = 6
 The possible longest increasing subsequences: [0, 2, 6, 9, 13, 15] or [0, 4, 6, 9, 11, 15] or [0, 4, 6, 9, 13, 15]
 
Input 3:
arr[] = {3, 10, 2, 1, 20}
Output: 3
Explanation: The longest increasing subsequence is 3, 10, 20

Input 4:
arr[] = {3, 2}
Output:1
Explanation: The longest increasing subsequences are {3} and {2}

Input 5:
arr[] = {50, 3, 10, 7, 40, 80}
Output: 4
Explanation: The longest increasing subsequence is {3, 7, 40, 80}
```

## Related Topics

- Array
- Binary Search
- Dynamic Programming
- Binary Indexed Tree
- Segment Tree

---
# Number of Longest Increasing Subsequence

Given an integer array nums, return the number of longest increasing subsequences.

Notice that the sequence has to be strictly increasing.

## Examples

Example 1:
```text
Input: nums = [1,3,5,4,7]
Output: 2
Explanation: The two longest increasing subsequences are [1, 3, 4, 7] and [1, 3, 5, 7].
```

Example 2:
```text
Input: nums = [2,2,2,2,2]
Output: 5
Explanation: The length of the longest increasing subsequence is 1, and there are 5 increasing subsequences of length 1,
so output 5.
```

## Related Topics

- Array
- Dynamic Programming
- Binary Indexed Tree
- Segment Tree

## Solution

The key intuition behind this algorithm is that for every position in the array, we figure out two things: the length of
the longest increasing subsequence that ends there, and how many such subsequences exist. By looking at all earlier
elements, we extend any subsequence that can grow by placing the current number at the end. Each time we form a longer
subsequence, we update both its length and its count, and if we find another way to reach the same length, we add those
counts as well. In the end, the longest subsequence length across all positions is known, and by summing how many
subsequences achieve that length, we determine the total number of longest increasing subsequences.

Using the intuition above, we implement the algorithm as follows:

1. Start by creating two arrays of the same size as the input: length to track the length of the longest increasing
   subsequence ending at each index, and count to track how many such subsequences end at that index. Initialize both
   arrays with 1 because every element alone forms an increasing subsequence of length 1
2. Initialize a variable, maxLen, with 1 to track the longest subsequence length found so far.
3. Iterate through each element in the array using index i. For each i:
   - Check all previous elements using index j, where j is less than i.
     - For each pair, check if nums[j] is less than nums[i]. If so:
       - If extending the subsequence from j creates a longer subsequence than what is currently recorded for i:
         - Update the length at i to be length[j] + 1.
         - Update count[i] to count[j] because all subsequences ending at j now extend to i.
       - Otherwise, if extending from j produces a subsequence of the same length as the best known for i:
         - Add count[j] to count[i]. This accumulates all valid ways to produce the same LIS length ending at i.
   - After processing all j for index i, update maxLen if length[i] is larger.
4. Initialize a variable, result, with 0 to accumulate the final count.
5. Scan through the length array to identify the indexes that achieved the maximum LIS length:
   - If length[i] equals maxLen, add count[i] to result.
6. Return result as the total number of longest increasing subsequences.

### Time Complexity

The algorithm’s time complexity is O(n^2), where n is the number of elements in nums. This is because for each element
in the array, we compare it with all previous elements to determine whether it can extend an increasing subsequence.
This results in a nested loop over the input size n.

### Space Complexity

The algorithm’s space complexity is O(n) because we use two additional arrays, length and count, each of size n.
