from typing import List
from collections import Counter
from heapq import heapify, heappop, heappush


def least_intervals_mathematical(tasks: List[str], n: int) -> int:
    """
    The time complexity of is O(N), where N is the number of tasks:
    Counter(tasks) takes O(N) time.
    The rest of the calculation is constant time, O(1), because the number of unique tasks (A-Z) is fixed at 26, meaning
     task_count.values() is at most 26 elements long.

     This greedy approach, which relies on the mathematical structure imposed by the most frequent task, is the most
     efficient way to solve the Task Scheduler problem.
    """
    # get the total number of tasks
    total_tasks = len(tasks)

    # Step 1: Use Counter to get all frequencies
    task_count = Counter(tasks)
    if not task_count:
        return 0

    # most_common() returns a list of (task, frequency) tuples
    # most_common(1) gives the highest frequency task: [('A', 3)] -> max_freq = 3
    max_freq = task_count.most_common(1)[0][1]

    # Step 2: Calculate how many tasks share the max frequency
    # This is slightly more efficient than looping through the full dictionary
    # because it stops checking once frequencies drop below max_freq.
    max_freq_count = sum(1 for freq in task_count.values() if freq == max_freq)

    # Step 3: Calculate the least number of intervals
    result = (max_freq - 1) * (n + 1) + max_freq_count

    # Step 4: Return the maximum of result and total tasks
    return max(result, total_tasks)


def least_intervals_with_max_heap(tasks: List[str], n: int) -> int:
    """
    Calculates the minimum CPU intervals required using an iterative Max Heap approach.

    This Max Heap solution is slightly less performant than the mathematical one, but it explicitly models the idle time
    (slots where max_heap is empty mid-cycle).

    Max Heap Complexity: O(T⋅KlogK), where T is the total number of intervals (can be up to N⋅n), and K is the number
    of unique tasks (at most 26).
    """
    # 1. Count Frequencies
    task_count = Counter(tasks)
    if not task_count:
        return 0

    time = 0
    # 2. Setup Max Heap (store negative frequencies for a Python Min Heap)
    # The task with the highest frequency will have the smallest negative value (e.g., -3).
    max_heap = [-freq for freq in task_count.values()]
    heapify(max_heap)

    # Loop continues until all tasks are executed (heap is empty)
    while max_heap:
        temp_list = []
        cycle_len = 0

        # Execute tasks for one cooling cycle (n + 1 slots)
        # We process up to n + 1 tasks, always picking the highest frequency one available.
        for _ in range(n + 1):
            if max_heap:
                # Pop the highest frequency task
                frequency = -heappop(max_heap)

                if frequency > 1:
                    # If the task needs to run again, store the remaining count
                    temp_list.append(frequency - 1)

                cycle_len += 1
            else:
                # Stop iterating slots if the heap is empty, though time will still advance.
                break

        # 3. Re-insert Tasks
        # Push the remaining counts back onto the heap (as negative values)
        for freq in temp_list:
            heappush(max_heap, -freq)

        # 4. Time Calculation
        if max_heap:
            # If the heap is NOT empty, it means there are still tasks remaining.
            # We must wait for the full cooling period, so we advance time by n + 1.
            time += n + 1
        else:
            # If the heap IS empty, it means all tasks were completed in this cycle.
            # We only count the intervals actually used (cycle_len).
            time += cycle_len

    return time
