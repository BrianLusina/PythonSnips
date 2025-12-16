# Meeting Rooms

Given an 2D integer array A of size N x 2 denoting time intervals of different meetings.

Where:

A[i][0] = start time of the ith meeting.
A[i][1] = end time of the ith meeting.

Find the minimum number of conference rooms required so that all meetings can be done.

> Note :- If a meeting ends at time t, another meeting starting at time t can use the same conference room

```plain
Input Format
The only argument given is the matrix A.
```

```plain
Output Format
Return the minimum number of conference rooms required so that all meetings can be done.
```

```plain
Example Input
Input 1:

A = [      [0, 30]
[5, 10]
[15, 20]
]

Input 2:

A =  [     [1, 18]
[18, 23]
[15, 29]
[4, 15]
[2, 11]
[5, 13]
]

Example Output
Output 1:

2
Output 2:

4
```

```plain
Example Explanation
Explanation 1:

Meeting one can be done in conference room 1 form 0 - 30.
Meeting two can be done in conference room 2 form 5 - 10.
Meeting three can be done in conference room 2 form 15 - 20 as it is free in this interval.
Explanation 2:

Meeting one can be done in conference room 1 from 1 - 18.
Meeting five can be done in conference room 2 from 2 - 11.
Meeting four can be done in conference room 3 from 4 - 15.
Meeting six can be done in conference room 4 from 5 - 13.
Meeting three can be done in conference room 2 from 15 - 29 as it is free in this interval.
Meeting two can be done in conference room 4 from 18 - 23 as it is free in this interval.
```

## Examples

![Example 1](./images/examples/meeting_rooms_example_1.png)
![Example 2](./images/examples/meeting_rooms_example_2.png)
![Example 3](./images/examples/meeting_rooms_example_3.png)

## Solution

### Naive Approach

The naive approach to solve this problem is to check each meeting’s interval with every other meeting’s interval to 
determine if a room is available or a new room needs to be allocated. Though this approach is easy, it becomes 
inefficient when there are a large number of meetings and their time intervals overlap. In the worst-case scenario, we 
would need to allocate a new room for each meeting, resulting in a time complexity of O(n^2), where n is the number of 
meetings. Therefore, while this approach can work for small inputs, it is not scalable and becomes impractical for 
larger inputs. So, let’s devise an optimized approach to solve this problem.

### Solution summary

To recap, the solution to this problem can be divided into the following four parts:

1. We sort the meeting intervals based on their start times. 
2. We maintain a min-heap and insert the end time of the first meeting. 
3. For each meeting, we check the following:
   - If the minimum end time is less than or equal to the start time of a new meeting, then a room is available.
   - If a meeting room is unavailable, a new room is allocated for the meeting.
4. The size of the heap after all meetings have been processed is equal to the minimum number of rooms required to 
   accommodate all meetings.

#### Time Complexity

Since we are sorting the intervals and also maintaining the heap, we have to take the time taken by these two processes 
into account. The sorting of the meeting intervals according to the start time takes `O(n × log(n))`. Now, for the heap, 
we know that we add the end time of a meeting if there is no room available for the meeting. Since the cost of adding an 
element to a heap is `O(log(size of heap))` in the worst case, the cost of adding to the heap grows in the following way:

log(1) + log(2) + log(3) + ... + log(n) = log(n!) = O(n log(n))

According to `Stirling’s approximation`, the sum of the above equation is O(n * log(n)). So, the total time complexity 
becomes O(n log(n)) + O(n log(n)) = O(n log(n)).

> Stirling's approximation is a mathematical formula that provides an approximate value for the factorial of a large 
> positive integer

#### Space Complexity

The space complexity of this solution is O(n). This is because we are building a min-heap that, in the worst case, 
can have all the input elements. Therefore, the space required to compute this solution would be O(n).
