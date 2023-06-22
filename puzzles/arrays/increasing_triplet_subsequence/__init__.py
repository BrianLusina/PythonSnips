from typing import List


def increasing_triplet(nums: List[int]) -> bool:
    for i in range(len(nums)):
        triplets = nums[i:i + 3]

        if len(triplets) == 3:
            if triplets[0] < triplets[1] < triplets[2]:
                return True

    return False

def increasingTriplet(nums: List[int]) -> bool:
    n = len(nums)
    max_right = [0] * n  # max_right[i] is the maximum element among nums[i+1...n-1]
    max_right[-1] = nums[-1]
    for i in range(n - 2, -1, -1):
        max_right[i] = max(max_right[i + 1], nums[i + 1])

    min_left = nums[0]
    for i in range(1, n - 1):
        if min_left < nums[i] < max_right[i]:
            return True
        min_left = min(min_left, nums[i])
    return False