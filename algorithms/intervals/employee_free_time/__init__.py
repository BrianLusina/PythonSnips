from typing import List, Tuple
import heapq
from algorithms.intervals.employee_free_time.interval import Interval


def employee_free_time(schedules: List[List[Interval]]) -> List[Interval]:
    """
    Finds intervals where employees have free time

    Complexity:
    Time Complexity: O(NlogN), where N is the total number of intervals across all employees. This is dominated by the sorting step.
    Space Complexity: O(N) to store the flattened all_schedules list.

    Args:
        schedules(list): a list of lists, where each inner list contains `Interval` objects representing an employee's schedule.
    Returns:
        list: Intervals of employee free time
    """
    # We need to combine and merge all employee intervals(schedules) into one unified schedule to be able to check
    # for free time. Since using a new list incurs a space cost of O(n), we can modify the input list, however, this
    # has side effects if the schedule list is used in other parts of the program. To avoid side effects, we copy over
    # the input list into a new list to handle the merging
    all_schedules: List[Interval] = []
    for schedule in schedules:
        for schedule_interval in schedule:
            all_schedules.append(schedule_interval)

    if not all_schedules:
        return []

    # sort by start time
    all_schedules.sort(key=lambda x: x.start)

    # Keep track of the latest meeting's end time. This is initialized the first schedule's end time
    latest_end = all_schedules[0].end

    # This will keep track of the free time slots
    free_time_slots: List[Interval] = []

    # Now we need to find the gaps in the combined schedule. Since we have already used the first schedule's end time
    # as the latest end we have seen so far, we start at the next interval.
    for idx in range(1, len(all_schedules)):
        current_schedule = all_schedules[idx]
        current_interval_start, current_interval_end = (
            current_schedule.start,
            current_schedule.end,
        )

        # If the current interval's start time is greater than the latest end time we have seen so far, it means we have
        # found free time
        if current_interval_start > latest_end:
            # we have a free time slot
            free_interval = Interval(start=latest_end, end=current_interval_start)
            free_time_slots.append(free_interval)

        # update the latest_end to the maximum of the latest end time seen so far
        latest_end = max(latest_end, current_interval_end)

    return free_time_slots


def employee_free_time_heap(schedules: List[List[Interval]]) -> List[Interval]:
    """
    Finds intervals where employees have free time using a min heap

    Args:
        schedules(list): a list of lists, where each inner list contains `Interval` objects representing an employee's schedule.
    Returns:
        list: Intervals of employee free time
    """
    heap: List[Tuple[int, int, int]] = []
    # Iterate for all employees' schedules
    # and add start of each schedule's first interval along with
    # its index value and a value 0.
    for i in range(len(schedules)):
        if schedules[i]:  # Only add if employee has at least one interval
            heap.append((schedules[i][0].start, i, 0))

    # Create heap from array elements.
    heapq.heapify(heap)

    # Handle empty heap
    if not heap:
        return []

    # Take an empty array to store results.
    free_time_slots = []

    # Set 'latest_end_time' to the start time of first interval in heap.
    latest_end_time = schedules[heap[0][1]][heap[0][2]].end

    # Iterate till heap is empty
    while heap:
        # Pop an element from heap and set value of employee_index and interval_index
        _, employee_index, interval_index = heapq.heappop(heap)

        # Select an interval
        schedule_interval = schedules[employee_index][interval_index]

        # If selected interval's start value is greater than the
        # latest_end_time value, it means that this interval is free.
        # So, add this interval (latest_end_time, interval's end value) into result.
        if schedule_interval.start > latest_end_time:
            free_time_slots.append(Interval(latest_end_time, schedule_interval.start))

        # Update the latest_end_time as maximum of latest_end_time and interval's end value.
        latest_end_time = max(latest_end_time, schedule_interval.end)

        # If there is another interval in current employees' schedule,
        # push that into heap.
        if interval_index + 1 < len(schedules[employee_index]):
            heapq.heappush(
                heap,
                (
                    schedules[employee_index][interval_index + 1].start,
                    employee_index,
                    interval_index + 1,
                ),
            )

    # When the heap is empty, return result.
    return free_time_slots
