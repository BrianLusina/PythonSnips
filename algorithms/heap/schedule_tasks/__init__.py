from typing import List
from heapq import heappush, heappop, heapify


def minimum_machines(tasks: List[List[int]]) -> int:
    # sort tasks by their start time in place, Time cost is O(n log(n)) with space cost being O(n) due to timsort
    tasks.sort(key=lambda x: x[0])

    # initialize a min heap to keep track of the end times
    machines: List[int] = []
    heapify(machines)

    for current_task in tasks:
        task_start, task_end = current_task
        # check if a machine with the earliest finish time is free
        if machines and machines[0] <= task_start:
            # reuse machine
            heappop(machines)

        # assign a machine to the current task
        heappush(machines, task_end)
    # Return the size of the heap representing the minimum number of machines required
    return len(machines)
