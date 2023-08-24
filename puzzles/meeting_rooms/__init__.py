from typing import List
import heapq


def find_minimum_meeting_rooms(meetings: List[List[int]]) -> int:
    """
    Uses 2 lists to find the minimum number of meeting rooms required

    Complexity:
    Time Complexity: O(n*log(n)) as we sort the 2 lists
    Space Complexity: O(n) we store the meetings in a list
    @param meetings: start and end times of meetings
    @return: minimum number of meeting rooms to allocated
    """
    if not meetings:
        return 0
    start_times, end_times = [], []

    for start, end in meetings:
        start_times.append(start)
        end_times.append(end)

    start_times.sort()
    end_times.sort()

    j = 0
    num_rooms = 0

    for i in range(len(start_times)):
        if start_times[i] < end_times[j]:
            num_rooms += 1
        else:
            j += 1

    return num_rooms


def find_minimum_meeting_rooms_priority_queue(meetings: List[List[int]]) -> int:
    """
    Uses a priority queue to find minimum number of meetings

    Complexity:
    Time Complexity: O(log(n)) as we sort the list
    Space Complexity: O(n) we store the meetings in a list
    @param meetings: start and end times of meetings
    @return: minimum number of meeting rooms to allocated
    """
    if not meetings:
        return 0

    # sort meetings in ascending order by start time
    meetings.sort(key=lambda x: x[0])

    # initialize heap & add first meeting's end
    rooms = []
    heapq.heappush(rooms, meetings[0][1])

    for start, end in meetings[1:]:
        # top of the heap is the meeting that will end soonest, we can remove it if it ends before the next meeting
        # starts
        if rooms[0] <= start:
            heapq.heappop(rooms)

        heapq.heappush(rooms, end)

    return len(rooms)
