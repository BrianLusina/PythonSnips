# Count Days Without Meetings

You are given a positive integer, `days`, which represents the total number of days an employee is available for work, 
starting from day 1. You are also given a 2D array, `meetings`, where each entry meetings[i] = [starti, endi] indicates 
that a meeting is scheduled from day starti to day endi (both inclusive).

Your task is to count the days when the employee is available for work but has no scheduled meetings.

> Note: The meetings may overlap.

## Constraints

- 1 <= days <= 10^5
- 1 <= meetings.length <= 10^3
- meetings[i].length == 2
- 1 <= `meetings[i][0]` <= `meetings[i][1]` <= days

## Examples

![Example 1](./images/examples/count_days_without_meetings_example_1.png)
![Example 2](./images/examples/count_days_without_meetings_example_2.png)
![Example 3](./images/examples/count_days_without_meetings_example_3.png)

## Solution

The core idea of this solution is to merge overlapping meetings into continuous intervals to efficiently track the 
occupied days. We begin by sorting the meetings to process them sequentially. As we iterate, we merge overlapping 
meetings while counting the occupied days whenever gaps appear. Finally, subtracting the total occupied days from the 
available days gives the number of free days.

Using the intuition above, we implement the algorithm as follows:

1. First, sort the meetings based on their start time to process them in order.
2. Initialize a variable, occupied, with 0 to count the days when the employee has scheduled meetings.
3. Initialize two variables, start and end, with the first meeting’s start and end times. These variables define the 
   beginning and end of the merged meeting interval to efficiently track continuously occupied periods.
4. Iterate through the remaining meetings:
   - If a meeting overlaps with the current merged meeting, extend the end time to merge it into the existing interval.
   - Otherwise, add the days of the merged meeting to occupied as `occupied = occupied + (end - start + 1)`. Then, update
     the start and end for the next interval.
5. After the loop, add the days of the last merged interval to occupied.
6. Return the difference between days and occupied (`days−occupied`), representing the number of days when the employee 
   is available for work but has no scheduled meetings.

![Solution 1](./images/solutions/count_days_without_meetings_solution_1.png)
![Solution 2](./images/solutions/count_days_without_meetings_solution_2.png)
![Solution 3](./images/solutions/count_days_without_meetings_solution_3.png)
![Solution 4](./images/solutions/count_days_without_meetings_solution_4.png)
![Solution 5](./images/solutions/count_days_without_meetings_solution_5.png)
![Solution 6](./images/solutions/count_days_without_meetings_solution_6.png)
![Solution 7](./images/solutions/count_days_without_meetings_solution_7.png)
![Solution 8](./images/solutions/count_days_without_meetings_solution_8.png)
![Solution 9](./images/solutions/count_days_without_meetings_solution_9.png)
![Solution 10](./images/solutions/count_days_without_meetings_solution_10.png)
![Solution 11](./images/solutions/count_days_without_meetings_solution_11.png)
![Solution 12](./images/solutions/count_days_without_meetings_solution_12.png)

### Time Complexity

The algorithm’s time complexity is O(nlogn), where n is the size of the meetings array. This is due to the sorting step, 
which dominates the overall complexity while merging the intervals runs in O(n).

### Space Complexity

The algorithm’s space complexity is constant, O(1).
