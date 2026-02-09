from typing import List, Tuple
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
        # Check if the minimum element of the heap (i.e., the earliest ending meeting) is free
        if rooms[0] <= start:
            # If the room is free, extract the earliest ending meeting and add the ending time of the current meeting
            heapq.heappop(rooms)

        # Add the ending time of the current meeting to the heap
        heapq.heappush(rooms, end)

    # The size of the heap tells us the number of rooms allocated
    return len(rooms)


def most_booked(meetings: List[List[int]], rooms: int) -> int:
    # A counter array that keeps track of the number of meetings held in each room
    counter = [0] * rooms
    # Min heap to keep track of free rooms
    available = [i for i in range(rooms)]
    # Min heap for rooms currently in use
    used_rooms: List[Tuple[int, int]] = []

    # Sort the meetings by their start times to process them in chronological order. This uses additional space as we
    # don't want to mutate the input meetings list. In addition, incurs time complexity of O(n log(n)) due to sorting
    sorted_meetings = sorted(meetings, key=lambda x: x[0])

    # For each meeting, free up rooms that have finished their meetings by moving them from used_rooms to available
    for meeting in sorted_meetings:
        current_start_time, current_end_time = meeting

        # If a room is free, assign it to the current meeting. If no rooms are fre, delay the meeting until the earliest
        # available room is free, then schedule it

        # Free up rooms that have finished their meetings by their current start time
        while used_rooms and used_rooms[0][0] <= current_start_time:
            used_room = heapq.heappop(used_rooms)
            end_time, room_number = used_room
            heapq.heappush(available, room_number)

        # If no rooms are available, delay the meeting until a room becomes free
        if not available:
            used_room = heapq.heappop(used_rooms)
            used_room_end_time, used_room_number = used_room
            current_end_time = used_room_end_time + (
                current_end_time - current_start_time
            )
            heapq.heappush(available, used_room_number)

        # Allocate the meeting to the available room with the lowest number
        available_room = heapq.heappop(available)
        heapq.heappush(used_rooms, (current_end_time, available_room))
        counter[available_room] += 1

    # Once all meetings are processed, return the room with the highest number of meetings from the counter array
    return counter.index(max(counter))
