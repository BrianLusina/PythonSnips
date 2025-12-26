from typing import List
from bisect import bisect_right, bisect_left


def full_bloom_flowers(flowers: List[List[int]], people: List[int]) -> List[int]:
    # if there are no flowers, then we can return an empty list
    if not flowers:
        return []

    # sorted list of start and end times for the periods of blooming flowers
    start_times = sorted([start for start, _ in flowers])
    end_times = sorted([end for _, end in flowers])

    # This keeps track of the number of flowers that are in full bloom at each person's arrival time
    result = []

    for persons_arrival_time in people:
        # Counts every flower that started at or before the arrival
        flowers_in_bloom_before_arrival = bisect_right(
            start_times, persons_arrival_time
        )
        # Counts only flowers that ended strictly before the arrival, leaving the ones ending at that time in the "blooming" tally.
        flowers_not_in_bloom_before_arrival = bisect_left(
            end_times, persons_arrival_time
        )
        count = flowers_in_bloom_before_arrival - flowers_not_in_bloom_before_arrival
        result.append(count)

    return result


def full_bloom_flowers_2(flowers: List[List[int]], people: List[int]) -> List[int]:
    starts = []
    ends = []

    for start, end in flowers:
        starts.append(start)
        ends.append(end + 1)

    starts.sort()
    ends.sort()
    ans = []

    for person in people:
        i = bisect_right(starts, person)
        j = bisect_right(ends, person)
        ans.append(i - j)

    return ans
