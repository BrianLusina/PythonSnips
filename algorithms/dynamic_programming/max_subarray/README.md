# Maximum sum in sub-array

Find the maximum sub-array in an array using Kadane's algorithm

[reference](https://en.wikipedia.org/wiki/Maximum_subarray_problem)

sub_arr_maxsum finds the sub-array or sub-arrays having this maximum value for their corresponding sums of elements. The
wanted function:

```plain
find_subarr_maxsum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == [[4, -1, 2, 1], 6]
```

If in the solution we have two or more arrays having the maximum sum value, the result will have an array of arrays in
the corresponding order of the array, from left to right.

```plain
find_subarr_maxsum([4, -1, 2, 1, -40, 1, 2, -1, 4]) == [[[4, -1, 2, 1], [1, 2, -1, 4]], 6]
# From left to right [4, -1, 2, 1] appears in the array before than [1, 2, -1, 4].
```

If the array does not have any sub-array with a positive sum of its terms, the function will return [[], 0].

## Solution

We’ll solve this problem using Kadane’s Algorithm. It’s a dynamic programming approach. The key idea is that we can
efficiently find the maximum subarray ending at any position based on the maximum subarray ending at the previous 
position.

The subproblem here is finding the maximum subarray sum that ends at a specific index i. We need to calculate this for
every index i in the array. The base case is the first element of the array, where both current subarray sum and maximum
subarray sum are initialized with the first element’s value. This is the starting point for solving the subproblems. At
each step, we reuse the previously computed maximum subarray sum to find the solution for the current subproblem.

The steps of the algorithm are given below:

1. Initialize two variables, current_sum and max_sum, with the value of the first element in the input list. These 
   variables are used to keep track of the current sum of the subarray being considered, and the maximum sum found so
   far.
2. Iterate through the input list, starting from the second element to the end of the list. Within the loop, perform the
   following steps:
   - If current_sum + nums[i] is smaller than nums[i], this indicates that starting a new subarray with nums[i] would
     yield a larger sum than extending the previous subarray. In such cases, reset current_sum to nums[i].
   - Compare the current max_sum with the updated current_sum. This step ensures that the max_sum always stores the
     maximum sum encountered so far.
3. After the loop completes, the function returns the max_sum, which represents the maximum sum of any contiguous
   subarray within the input list.

### Time Complexity
The time complexity of this solution is O(n) because we are iterating the array once, where n is the total number of
elements in the array.

### Space Complexity

The space complexity of this solution is O(1).

---

# Maximum Sum Circular Subarray

Given a circular integer array nums of length n, return the maximum possible sum of a non-empty subarray of nums.

A circular array means the end of the array connects to the beginning of the array. Formally, the next element of
nums[i] is nums[(i + 1) % n] and the previous element of nums[i] is nums[(i - 1 + n) % n].

A subarray may only include each element of the fixed buffer nums at most once. Formally, for a subarray nums[i],
nums[i + 1], ..., nums[j], there does not exist i <= k1, k2 <= j with k1 % n == k2 % n.

## Examples

Example 1:

```text
Input: nums = [1,-2,3,-2]
Output: 3
Explanation: Subarray [3] has maximum sum 3.
```

Example 2:
```text
Input: nums = [5,-3,5]
Output: 10
Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10.
```

Example 3:

```text
Input: nums = [-3,-2,-3]
Output: -2
Explanation: Subarray [-2] has maximum sum -2.
```

## Constraints

- n == nums.length
- 1 <= n <= 3 * 104
- -3 * 104 <= nums[i] <= 3 * 10^4

## Topics

- Array
- Divide and Conquer
- Dynamic Programming
- Queue
- Monotonic Queue
