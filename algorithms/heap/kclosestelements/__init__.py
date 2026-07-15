from typing import List
import heapq
from algorithms.search.binary_search import binary_search


def k_closest(nums: List[int], k: int, target: int):
    heap = []

    for num in nums:
        diff = abs(num - target)

        if len(heap) < k:
            heapq.heappush(heap, (-diff, num))
        elif diff < -heap[0][0]:
            heapq.heappushpop(heap, (-diff, num))

    distances = [pair[1] for pair in heap]
    distances.sort()
    return distances


def find_closest_elements(nums: List[int], k: int, target: int):
    # If the length of 'nums' is the same as k, return 'nums'
    if len(nums) == k:
        return nums

    # if target is less than or equal to first element in 'nums',
    # return the first k elements from 'nums'
    if target <= nums[0]:
        return nums[0:k]

    # if target is greater than or equal to last element in 'nums',
    # return the last k elements from 'nums'
    if target >= nums[-1]:
        return nums[len(nums) - k : len(nums)]

    # find the first closest element to target using binary search
    first_closest = binary_search(nums, target, modified=True)

    # initilaize the sliding window pointers
    window_left = first_closest - 1
    window_right = window_left + 1

    # expand the sliding window untill its size becomes equal to k
    while (window_right - window_left - 1) < k:
        # if window's left pointer is going out of bounds move the window rightward
        if window_left == -1:
            window_right += 1
            continue

        # if window's right pointer is going out of bounds
        # OR if the element pointed to by window's left pointer is closer to target than
        # the element pointed to by window's right pointer, move the window leftward
        if window_right == len(nums) or abs(nums[window_left] - target) <= abs(
            nums[window_right] - target
        ):
            window_left -= 1

        # if the element pointed to by window's right pointer is closer to target than
        # the element pointed to by window's left pointer, move the window rightward
        else:
            window_right += 1

    # return k closest elements present inside the window
    return nums[window_left + 1 : window_right]
