# Split Array Largest Sum

Given an integer list nums and an integer k, split nums into k non-empty subarrays such that the largest sum among these
subarrays is minimized. The task is to find the minimized largest sum by choosing the split such that the largest sum of
every split of subarrays is the minimum among the sum of other splits.

## Constraints

- 1 <= nums.length <= 1000
- 0 <= nums[i] <= 10^4
- 1 <= k <= nums.length

## Examples

![Example 1](images/examples/split_array_largest_sum_example_1.png)
![Example 2](images/examples/split_array_largest_sum_example_2.png)
![Example 3](images/examples/split_array_largest_sum_example_3.png)
![Example 4](images/examples/split_array_largest_sum_example_4.png)

## Topics

- Array
- Binary Search
- Dynamic Programming
- Greedy
- Prefix Sum

## Solution

In a brute force method, you would try all possible ways to split the array into k subarrays, calculate the largest sum
for each split, and then find the smallest among those largest sums. This approach is extremely inefficient because the
number of ways to split the array grows exponentially as the size increases.

We reverse the process by guessing a value for the minimum largest sum and checking if it’s feasible:

- Instead of iterating through all splits, we only focus on testing whether a specific value allows us to split the
  array into k subarrays.

- But wait—just because one value works doesn’t mean it’s the smallest feasible value. We keep exploring smaller values
  to achieve the most optimized result.

The solution uses the binary search approach to find the optimal largest subarray sum without testing all possible splits.
The binary search finds the smallest possible value of the largest subarray sum and applies searching over the range of
possible values for this largest sum. But how do we guess this value? We guess the value using a certain range.
Here’s how:

- **Left boundary**: The maximum element in the array is the minimum possible value for the largest subarray sum. This
  is because any valid subarray must have a sum at least as large as the largest element.

- **Right boundary**: The maximum possible value for the largest subarray sum is the sum of all elements in the array.
  You would get this sum if the entire array were one single subarray.

The binary search iteratively tests midpoints in the above ranges. It determines whether dividing the array results in
at most k subarrays will result in the smallest largest sum. If it does, the search shifts to lower values to minimize
the largest sum. Otherwise, it shifts to higher values. Still, there might be subarrays whose sum could be smaller, so
the search keeps going until the search range crosses each other, i.e., **left boundary** > **right boundary**.

Here’s the step-by-step implementation of the solution:

- Start by initializing the ranges for search. The left will be the largest number in the array, and the right will be
  the sum of all numbers.
- Use a guessing approach. Start by considering a mid value between the left and right as a test value.
- Check if it is possible to divide the array into k subarrays so that the sum of no subarray is greater than mid.
  - Start with an empty sum and add numbers from the array. If adding the next number exceeds mid:
    - Start a new subarray with that number and increment the count of the subarrays.
  - Return FALSE if the count exceeds k. Otherwise, return TRUE.
- Adjust the guessing range by checking if the number of subarrays needed is within the k and reduce the mid to see if
  a smaller largest sum is possible.
- Otherwise, if the count of subarrays is more than k:
  - Increase the mid to make larger groups possible.
- Continue adjusting the mid until left < right. Return left as it contains the minimized largest possible sum.

- Let’s look at the following illustrations to get a better understanding of the solution:

![Solution 1](images/solutions/split_array_largest_sum_solution_1.png)
![Solution 2](images/solutions/split_array_largest_sum_solution_2.png)
![Solution 3](images/solutions/split_array_largest_sum_solution_3.png)
![Solution 4](images/solutions/split_array_largest_sum_solution_4.png)
![Solution 5](images/solutions/split_array_largest_sum_solution_5.png)
![Solution 6](images/solutions/split_array_largest_sum_solution_6.png)
![Solution 7](images/solutions/split_array_largest_sum_solution_7.png)
![Solution 8](images/solutions/split_array_largest_sum_solution_8.png)
![Solution 9](images/solutions/split_array_largest_sum_solution_9.png)
![Solution 10](images/solutions/split_array_largest_sum_solution_10.png)
![Solution 11](images/solutions/split_array_largest_sum_solution_11.png)
![Solution 12](images/solutions/split_array_largest_sum_solution_12.png)
![Solution 13](images/solutions/split_array_largest_sum_solution_13.png)
![Solution 14](images/solutions/split_array_largest_sum_solution_14.png)
![Solution 15](images/solutions/split_array_largest_sum_solution_15.png)
![Solution 16](images/solutions/split_array_largest_sum_solution_16.png)
![Solution 17](images/solutions/split_array_largest_sum_solution_17.png)
![Solution 18](images/solutions/split_array_largest_sum_solution_18.png)
![Solution 19](images/solutions/split_array_largest_sum_solution_19.png)
![Solution 20](images/solutions/split_array_largest_sum_solution_20.png)

### Time Complexity

The time complexity of this solution is O(n log(m)), where n is the length of the input array, and m is the difference
between `max(nums)` and `sum(nums)` because the range of possible sums considered during the binary search is from
`max(nums)`to `sum(nums)`. This range size determines the number of iterations in the binary search. The tighter this
range, the fewer iterations are needed. However, in the worst case, it spans the full difference: `sum(nums) - max(nums)`.
The time complexity becomes `n log(m)` because the `can_split` function is called `n` times for each iteration.

### Space Complexity

The time complexity of this solution is O(1) because only constant space is used.
