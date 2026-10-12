import heapq


def get_final_state(nums: list[int], k: int, multiplier: int) -> list[int]:
    if k == 0 or multiplier == 1:
        return nums

    min_heap = [(value, idx) for idx, value in enumerate(nums)]
    heapq.heapify(min_heap)

    for _ in range(k):
        _, idx = heapq.heappop(min_heap)
        nums[idx] *= multiplier
        heapq.heappush(min_heap, (nums[idx], idx))

    return nums


def get_final_state_full_scan(nums: list[int], k: int, multiplier: int) -> list[int]:
    if k == 0 or multiplier == 1:
        return nums

    n = len(nums)

    for _ in range(k):
        # Find the index of the smallest element in the array
        min_index = 0
        for i in range(n):
            if nums[i] < nums[min_index]:
                min_index = i

        # Multiply the smallest element by the multiplier
        nums[min_index] *= multiplier

    return nums
