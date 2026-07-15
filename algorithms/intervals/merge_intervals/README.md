# Merge Intervals

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array
of the non-overlapping intervals that cover all the intervals in the input.

## Constraints

- 1 ≤ `intervals.length` ≤ 10^3
- `intervals[i].length` == 2
- 0 ≤ `starti` ≤ `endi` ≤ 10^4


Example 1:
```text
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
```

Example 2:
```text
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
```

## Solution

### Naive Approach

The naive approach to merging intervals involves comparing each interval with all the intervals that come after it. If 
two intervals overlap, they are merged into a single interval by updating the start to the minimum of both start times 
and the end to the maximum of both end times. After merging, the second interval (the one being compared) is removed 
from the list, as its range is now included in the updated interval. The algorithm then checks for further overlaps with
the updated interval from the same position. This process repeats until all overlapping intervals have been merged, 
resulting in a final list of non-overlapping intervals.

This process continues until all overlapping intervals are merged. While this method is easy to understand and doesn’t 
require extra space, it can be inefficient for large inputs because it compares each interval with many others, leading 
to a time complexity of O(n^2).

### Optimized approach using the intervals pattern

The optimized approach starts by sorting the intervals in ascending order based on their start times. This step ensures
overlapping intervals are positioned next to each other, making identifying and merging them easier. Once sorted, the 
algorithm initializes a result list with the first interval. It then iterates through the remaining intervals one by 
one, comparing each to the last interval in the result list.

If the current interval overlaps with the last one in the result (i.e., its start time is less than or equal to the end 
time of the last interval), the two intervals are merged by updating the end time to the maximum of both intervals’ end 
times. If there is no overlap, the current interval is added to the result list as a new entry. This process continues 
until all intervals have been processed. In the end, the result list contains the merged, non-overlapping intervals.

#### Solution summary

To recap, the solution to this problem can be divided into the following two parts:

1. Sort the intervals list according to the start time.
2. Add the first interval from the sorted list to the output list. 
3. Then, iterate through the remaining intervals one by one. For each interval, check if it overlaps with the last 
   interval in the output list:
   - If they overlap, merge them by updating the end time to the maximum of both end times, and update the last interval 
     in the output list.
   - If they don’t overlap, simply append the current interval to the output list as a separate entry.

#### Time Complexity

The time complexity of this solution is O(n log n) where n is the number of intervals. This is because we need to sort 
the intervals list, which takes O(n log n) time. 

#### Space Complexity

The space complexity is O(n) for storing the result list. However, we do not count the space used merely for input and 
output in the space complexity calculation. Apart from the space required by the built-in sorting algorithm, the space 
complexity is O(1).
