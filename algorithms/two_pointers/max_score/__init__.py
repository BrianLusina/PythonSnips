from typing import List


def max_sum(nums1: List[int], nums2: List[int]) -> int:
    pointer_one, pointer_two = 0, 0
    sum_path_one, sum_path_two = 0, 0
    len_nums_1, len_nums_2 = len(nums1), len(nums2)
    mod = (10**9) + 7

    while pointer_one < len_nums_1 or pointer_two < len_nums_2:
        if pointer_one < len_nums_1 and (
            pointer_two == len_nums_2 or nums1[pointer_one] < nums2[pointer_two]
        ):
            sum_path_one += nums1[pointer_one]
            pointer_one += 1
        elif pointer_two < len_nums_2 and (
            pointer_one == len_nums_1 or nums1[pointer_one] > nums2[pointer_two]
        ):
            sum_path_two += nums2[pointer_two]
            pointer_two += 1
        else:
            sum_path_one = sum_path_two = (
                max(sum_path_one, sum_path_two) + nums1[pointer_one]
            )
            pointer_one += 1
            pointer_two += 1

    return max(sum_path_one, sum_path_two) % mod
