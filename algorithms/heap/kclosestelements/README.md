# Find K Closest Elements

Given a sorted array nums, a target value target, and an integer k, find the k closest elements to target in the array,
where "closest" is the absolute difference between each element and target. Return these elements in array, sorted in
ascending order.

## Examples

```text
nums = [-1, 0, 1, 4, 6]
target = 1
k = 3

Output
[-1, 0, 1]

Explanation
Explanation: -1 is 2 away from 1, 0 is 1 away from 1, and 1 is 0 away from 1. All other elements are more than 2 away. 
Since we need to return the elements in ascending order, the answer is [-1, 0, 1]
```

```text
nums = [5, 6, 7, 8, 9]
target = 10
k = 2

Output:
[8, 9]
```
