# Move Zeroes

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero
elements.

Note that you must do this in-place without making a copy of the array.

```plain

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
```

## Related Topics

- Array
- Two Pointers

## Solution

We can solve this problem by keeping a pointer i that iterates through the array and another pointer nextNonZero that
points to the position where the next non-zero element should be placed. We can then swap the elements at i and nextNonZero
if the element at i is non-zero. This way, we can maintain the relative order of the non-zero elements while moving all
the zeroes to the end of the array.

![Solution 1](./images/solutions/move_zeroes_solution_1.png)
![Solution 2](./images/solutions/move_zeroes_solution_2.png)
![Solution 3](./images/solutions/move_zeroes_solution_3.png)
![Solution 4](./images/solutions/move_zeroes_solution_4.png)
![Solution 5](./images/solutions/move_zeroes_solution_5.png)
![Solution 6](./images/solutions/move_zeroes_solution_6.png)
![Solution 7](./images/solutions/move_zeroes_solution_7.png)
![Solution 8](./images/solutions/move_zeroes_solution_8.png)
![Solution 9](./images/solutions/move_zeroes_solution_9.png)
![Solution 10](./images/solutions/move_zeroes_solution_10.png)
![Solution 11](./images/solutions/move_zeroes_solution_1.png)
![Solution 12](./images/solutions/move_zeroes_solution_12.png)
![Solution 13](./images/solutions/move_zeroes_solution_13.png)
