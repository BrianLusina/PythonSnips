# Meeting Rooms

Problem Description

```plain
Given an 2D integer array A of size N x 2 denoting time intervals of different meetings.

Where:

A[i][0] = start time of the ith meeting.
A[i][1] = end time of the ith meeting.

Find the minimum number of conference rooms required so that all meetings can be done.

Note :- If a meeting ends at time t, another meeting starting at time t can use the same conference room
```

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
