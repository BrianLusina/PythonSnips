from typing import List


def sort_array_by_parity_2(nums: List[int]) -> List[int]:
    if not nums:
        return []
    # Initialize two pointers:
    # even_idx moves across even indexes [0, 2, 4,..]
    # odd_idx moves across odd indexes [1, 3, 5,..]
    even_idx = 0
    odd_idx = 1

    # Traverse the array while both pointers are within bounds
    while even_idx < len(nums) and odd_idx < len(nums):
        # If number at even index 'i' is even, it's correctly placed
        if nums[even_idx] % 2 == 0:
            # Move to the next even index
            even_idx += 2
        # If number at odd index 'j' is odd, it's correctly placed
        elif nums[odd_idx] % 2 == 1:
            # Move to the next odd index
            odd_idx += 2
        else:
            # If misplaced (odd at even index or even at odd index), swap them
            nums[even_idx], nums[odd_idx] = nums[odd_idx], nums[even_idx]
            # Move both pointers forward after swapping
            even_idx += 2
            odd_idx += 2

    return nums
