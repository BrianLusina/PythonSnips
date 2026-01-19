# Maximum Sum of Subarray with Size K

Given an array of integers nums and an integer k, find the maximum sum of any contiguous subarray of size k.

## Examples

Example 1

```text
Input: nums = [2, 1, 5, 1, 3, 2], k = 3
Output: 9
Explanation: The subarray with the maximum sum is [5, 1, 3] with a sum of 9.
```

## Solution

We start by extending the window to size k. Whenever our window is of size k, we first compute the sum of the window and
update max_sum if it is larger than max_sum. Then, we contract the window by removing the leftmost element to prepare for
the next iteration. Note how we calculate the sum of the window incrementally by adding the new element and removing from
the previous sum.

![Solution 1](./images/solutions/max_sum_of_subarray_size_k_solution_1.png)
![Solution 2](./images/solutions/max_sum_of_subarray_size_k_solution_2.png)
![Solution 3](./images/solutions/max_sum_of_subarray_size_k_solution_3.png)
![Solution 4](./images/solutions/max_sum_of_subarray_size_k_solution_4.png)
![Solution 5](./images/solutions/max_sum_of_subarray_size_k_solution_5.png)
![Solution 6](./images/solutions/max_sum_of_subarray_size_k_solution_6.png)
![Solution 7](./images/solutions/max_sum_of_subarray_size_k_solution_7.png)
![Solution 8](./images/solutions/max_sum_of_subarray_size_k_solution_8.png)
![Solution 9](./images/solutions/max_sum_of_subarray_size_k_solution_9.png)
![Solution 10](./images/solutions/max_sum_of_subarray_size_k_solution_10.png)
![Solution 11](./images/solutions/max_sum_of_subarray_size_k_solution_11.png)
![Solution 12](./images/solutions/max_sum_of_subarray_size_k_solution_12.png)
![Solution 13](./images/solutions/max_sum_of_subarray_size_k_solution_13.png)
![Solution 14](./images/solutions/max_sum_of_subarray_size_k_solution_14.png)
![Solution 15](./images/solutions/max_sum_of_subarray_size_k_solution_15.png)
![Solution 16](./images/solutions/max_sum_of_subarray_size_k_solution_16.png)
![Solution 17](./images/solutions/max_sum_of_subarray_size_k_solution_17.png)
