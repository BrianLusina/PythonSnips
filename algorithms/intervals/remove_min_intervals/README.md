# Non-overlapping Intervals

Given an array of intervals `intervals` where `intervals[i] = [starti, endi)` contains the half-open interval (start, endi),
return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

> A half-open interval is one that contains only one of its boundary elements. The “(” parenthesis denotes the exclusion
> of the starting point. The “]” bracket denotes the inclusion of the ending point.

Note that intervals which only touch at a point are non-overlapping. For example, [1, 2] and [2, 3] are non-overlapping.

> Note: Two intervals (a,b] and (c,d] are considered overlapping if there exists a value x such that a<x≤b and c<x≤d. In
> other words, if there is any point within both intervals (excluding their starting points) where both intervals have
> values, they are considered overlapping. For example, the intervals (7,11] and (10,12] are overlapping, whereas the
> intervals (2,4] and (4,5] are non-overlapping.

## Examples

Example 1:
```text
Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.
```

Example 2:
```text
Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.
```

Example 3:
```text
Input: intervals = [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
```

## Constraints

- 1 <= intervals.length <= 10^5
- intervals[i].length == 2
- -5 * 10^4 <= starti < endi <= 5 * 10^4

## Topics

- Array
- Dynamic Programming
- Greedy
- Sorting

## Solution

1. Sort the intervals array in an ascending order based on the end time of each interval.
2. Declare two variables that will assist us in the algorithm:
   - end: This stores the end time of the last included interval.
   - remove: This stores the number of intervals to be removed. It is initialized to 
3. Traverse the sorted intervals array to determine which interval needs to be excluded. For each interval, the following
   conditions are checked:
   - If the start time of the current interval is greater than or equal to end, this interval does not overlap with the
     previously included interval and can be included. Therefore, we update end to the end time of the current interval,
     which is the next earliest possible end time.
   - Otherwise, the current interval overlaps with the previously included intervals. Therefore, it must be removed, so
     we increment remove.
4. After the sorted intervals array has been traversed completely, there are no more intervals left to evaluate, so we
   return remove, which now contains the minimum number of intervals to be removed.

### Time Complexity

The time complexity of this solution is O(n log(n)), where n is the length of the `intervals` array.

Explanation:

- Time taken to sort the intervals array: O(nlog(n))
- Time taken to traverse the intervals array: O(n)

Therefore, the overall time complexity becomes O(n + n log(n)), which simplifies to O(nlog(n)).

### Space Complexity

The space complexity of this solution is O(1).
