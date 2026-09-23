import heapq
from collections import defaultdict
from math import inf


def max_events(events: list[list[int]]) -> int:
    if not events:
        return 0
    number_of_events = len(events)
    max_day = max(event[1] for event in events)
    sorted_events = sorted(events)
    pq = []
    result, j = 0, 0

    for i in range(1, max_day + 1):
        while j < number_of_events and sorted_events[j][0] <= i:
            heapq.heappush(pq, sorted_events[j][1])
            j += 1

        while pq and pq[0] < i:
            heapq.heappop(pq)

        if pq:
            heapq.heappop(pq)
            result += 1

    return result


def max_events_2(events: list[list[int]]) -> int:
    if not events:
        return 0
    # Sort events by start day
    events.sort(key=lambda x: x[0])

    min_heap = []  # Min-heap of event end days available to attend
    event_index = 0  # Pointer into sorted events
    attended_count = 0  # Total events attended
    max_day = max(event[1] for event in events)

    # Iterate day by day from 1 to max possible day
    for currentDay in range(1, max_day + 1):
        # Add all events that start today to the heap (by their end day)
        while event_index < len(events) and events[event_index][0] == currentDay:
            heapq.heappush(min_heap, events[event_index][1])
            event_index += 1

        # Remove events that already ended before today
        while min_heap and min_heap[0] < currentDay:
            heapq.heappop(min_heap)

        # Attend the event that ends the earliest (greedy)
        if min_heap:
            heapq.heappop(min_heap)
            attended_count += 1

        # If no future events remain and heap is empty, we can stop early
        if event_index == len(events) and not min_heap:
            break

    return attended_count


def max_events_3(events: list[list[int]]) -> int:
    if not events:
        return 0

    # Group events by their start day
    events_by_start_day = defaultdict(list)

    # Find the range of days we need to consider
    min_start_day = inf
    max_end_day = 0

    for start_day, end_day in events:
        events_by_start_day[start_day].append(end_day)
        min_start_day = min(min_start_day, start_day)
        max_end_day = max(max_end_day, end_day)

    # Min heap to store end days of available events
    available_events = []
    attended_events = 0

    # Process each day in the range
    for current_day in range(min_start_day, max_end_day + 1):
        # Remove events that have already ended (end day < current day)
        while available_events and available_events[0] < current_day:
            heapq.heappop(available_events)

        # Add all events starting on the current day to the heap
        # Store their end days in the heap
        for end_day in events_by_start_day[current_day]:
            heapq.heappush(available_events, end_day)

        # Attend the event that ends earliest (greedy approach)
        if available_events:
            heapq.heappop(available_events)
            attended_events += 1

    return attended_events
