from typing import List, Dict


def check_subarray_sum(nums: List[int], k: int) -> bool:
    # This keeps track of the cumulative sum, but we only care about its remainder when divided by k.
    cumulative_sum = 0

    # This is a remainder to index mapping to store where a remainder was calculated and at what index. This helps with
    # constant time lookups
    # Setting {0: -1} handles the case where a "good" subarray starts right from the beginning of the array. If the
    # running_sum % k becomes 0 at index 1, the length calculation 1−(−1)=2 correctly identifies a valid subarray. 📏
    remainder_map: Dict[int, int] = {0: -1}

    for idx, num in enumerate(nums):
        # Compute the remainder of the cumulative sum with k
        remainder = (cumulative_sum + num) % k

        # Check if the remainder has been seen before
        if remainder in remainder_map:
            # Ensure the subarray length is at least 2
            if idx - remainder_map[remainder] >= 2:
                return True
        else:
            # Store the first occurrence of the remainder
            remainder_map[remainder] = idx

    return False
