# Employee Free Time

You’re given a list containing the schedules of multiple employees. Each person’s schedule is a list of non-overlapping 
intervals in sorted order. An interval is specified with the start and end time, both being positive integers. Your task 
is to find the list of finite intervals representing the free time for all the employees.

> Note: The common free intervals are calculated between the earliest start time and the latest end time of all meetings 
across all employees.

## Constraints

- 1 <= `schedule.length`, `schedule[i].length` <= 50
- 0 <= `interval.start`, `interval.end` <= 10^8, where `interval` is any interval in the list of schedules

## Examples

![Example 1](./images/examples/employee_free_time_example_1.png)
![Example 2](./images/examples/employee_free_time_example_2.png)
![Example 3](./images/examples/employee_free_time_example_3.png)

## Solution

The solution’s core revolves around merging overlapping intervals of employees and identifying the free time gaps 
between these merged intervals. Using a min-heap, we arrange the intervals based on when they start, sorting them 
according to their start times. When we pop an element from the min-heap, it guarantees that the earliest available 
interval is returned for processing. As intervals are popped from the min-heap, the algorithm attempts to merge them. 
If the currently popped interval’s start time exceeds the merged interval’s end time, a gap is identified, indicating a
free period. After identifying each gap, the algorithm restarts the merging process to continue identifying additional
periods of free time.

We use the following variables in our solution:

- `latest_end_time`: Stores the end time of the previously processed interval. 
- `employee_index`: Stores the employee’s index value. 
- `interval_index`: Stores the interval’s index of the employee, i. 
- `free_time_slots`: Stores the free time intervals.

The steps of the algorithm are given below :
- We store the start time of each employee’s first interval, along with its index value and a value of 0, in a min-heap.
- We set previous to the start time of the first interval present in a heap.
- Then, we iterate a loop until the heap is empty, and in each iteration, we do the following:
  - Pop an element from the min-heap and set `employee_index` and `interval_index` to the second and third values, 
    respectively, from the popped value. 
  - Select the interval from the input located at `employee_index`,`interval_index`. 
  - If the selected interval’s start time is greater than `latest_end_time`, it means that the time from `latest_end_time`
    to the selected interval’s start time is free. So, add this interval to the `free_time_slots` array. 
  - Now, update the `latest_end_time` as `max(latest_end_time, end time of selected interval)`. 
  - If the current employee has any other interval, push it into the heap.
- After all the iterations, when the heap becomes empty, return the `free_time_slots` array.

![Solution 1](./images/solutions/employee_free_time_heap_solution_1.png)
![Solution 2](./images/solutions/employee_free_time_heap_solution_2.png)
![Solution 3](./images/solutions/employee_free_time_heap_solution_3.png)
![Solution 4](./images/solutions/employee_free_time_heap_solution_4.png)
![Solution 5](./images/solutions/employee_free_time_heap_solution_5.png)
![Solution 6](./images/solutions/employee_free_time_heap_solution_6.png)
![Solution 7](./images/solutions/employee_free_time_heap_solution_7.png)

### Time Complexity

The time complexity of this algorithm is O(mlog(n)), where n is the number of employees and m is the total number of 
intervals across all employees. This is because the time complexity of filling the heap is O(nlog(n)) and the time 
complexity of processing the heap is O(mlog(n)).

### Space Complexity

We use a heap in the solution, which can have a maximum of n elements. Hence, the space complexity of this solution is 
O(n), where n is the number of employees.
