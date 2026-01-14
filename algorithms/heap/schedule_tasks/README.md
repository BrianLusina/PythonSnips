# Schedule Tasks on Minimum Machines

We are given an input array, tasks, where tasks[i]=[starti ,endi] represents the start and end times of n tasks. Our
goal is to schedule these tasks on machines given the following criteria:

- A machine can execute only one task at a time. 
- A machine can begin executing a new task immediately after completing the previous one. 
- An unlimited number of machines are available.

Find the minimum number of machines required to complete these n tasks.

## Constraints

- n == `tasks.length`
- 1 <= `tasks.length` <= 10^3
- 0 <= `tasks[i].start` < `tasks[i].end` <= 10^4

## Examples

![Example 1](images/examples/schedule_tasks_on_minimum_machines_example_1.png)
![Example 2](images/examples/schedule_tasks_on_minimum_machines_example_2.png)
![Example 3](images/examples/schedule_tasks_on_minimum_machines_example_3.png)
![Example 4](images/examples/schedule_tasks_on_minimum_machines_example_4.png)

## Solution

The core intuition for solving this problem is to allocate tasks to the minimum number of machines by reusing machines 
whenever possible. The algorithm efficiently manages machine availability by sorting tasks by their start times and using
a min heap to track end times. If the earliest available machine (top of the heap) finishes before or as a task starts,
it is reused and removed from the heap. Otherwise, a new machine is allocated, and the current task’s end time is pushed
into the heap. The heap size at the end represents the minimum number of machines required.

Using the intuition above, we implement the algorithm as follows:

1. Sort the tasks array by the start time of each task to process them in chronological order. 
2. Initialize a min heap (machines) to keep track of the end times of tasks currently using machines. 
3. Iterate over each task in the sorted tasks array. 
   - Extract the start and end times of the current task. 
   - Check if the machine with the earliest finish time is free, i.e., top of machines is less than or equal to the
     current task’s start time. If it is, remove it from the heap, as the machine can be reused. 
   - Push the end time of the current task into the heap, indicating that a machine is now in use until that time. 
4. After processing all tasks, return the size of the heap, which represents the minimum number of machines required.

![Solution 1](images/solutions/schedule_tasks_on_minimum_machines_solution_1.png)
![Solution 2](images/solutions/schedule_tasks_on_minimum_machines_solution_2.png)
![Solution 3](images/solutions/schedule_tasks_on_minimum_machines_solution_3.png)
![Solution 4](images/solutions/schedule_tasks_on_minimum_machines_solution_4.png)
![Solution 5](images/solutions/schedule_tasks_on_minimum_machines_solution_5.png)
![Solution 6](images/solutions/schedule_tasks_on_minimum_machines_solution_6.png)
![Solution 7](images/solutions/schedule_tasks_on_minimum_machines_solution_7.png)
![Solution 8](images/solutions/schedule_tasks_on_minimum_machines_solution_8.png)
![Solution 9](images/solutions/schedule_tasks_on_minimum_machines_solution_9.png)
![Solution 10](images/solutions/schedule_tasks_on_minimum_machines_solution_10.png)
![Solution 11](images/solutions/schedule_tasks_on_minimum_machines_solution_11.png)
![Solution 12](images/solutions/schedule_tasks_on_minimum_machines_solution_12.png)
![Solution 13](images/solutions/schedule_tasks_on_minimum_machines_solution_13.png)
![Solution 14](images/solutions/schedule_tasks_on_minimum_machines_solution_14.png)
![Solution 15](images/solutions/schedule_tasks_on_minimum_machines_solution_15.png)
![Solution 16](images/solutions/schedule_tasks_on_minimum_machines_solution_16.png)
![Solution 17](images/solutions/schedule_tasks_on_minimum_machines_solution_17.png)
![Solution 18](images/solutions/schedule_tasks_on_minimum_machines_solution_18.png)
![Solution 19](images/solutions/schedule_tasks_on_minimum_machines_solution_19.png)

### Time Complexity

The time complexity of the above algorithm is O(nlogn), where n is the number of tasks represented by the length of the
tasks array. This is because:

- Sorting the array takes O(nlogn). 
- The total cost for heap operations is O(nlogn) because we process n tasks, and each operation on the min-heap has a
  time complexity of O(logn).

Therefore, the overall time complexity is O(nlogn).

### Space Complexity

The algorithm’s space complexity is O(n) because the min heap can grow up to a maximum size of n if every task requires
a separate machine.
