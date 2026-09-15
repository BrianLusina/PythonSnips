from typing import List


def get_k_sum_subsets(nums: List[int], k: int) -> List[List[int]]:
    def get_k_sum_subsets_helper(num_list: List[int], partial: List[int]):
        # sum the partial list
        list_sum = sum(partial)
        # If sum is equal to target_sum, add the set from the partial_list to the output
        if list_sum == k and len(partial) > 0:
            subsets.append(partial)
        elif list_sum > k:
            return
        else:
            for i in range(0, len(num_list)):
                new_partial_list = partial[0:]
                new_partial_list.append(num_list[i])
                new_list = num_list[i + 1 :]

                get_k_sum_subsets_helper(new_list, new_partial_list)

    partial_list = []
    subsets = []
    get_k_sum_subsets_helper(nums, partial_list)
    return subsets


def get_k_sum_subsets_backtrack(arr: List[int], k: int) -> List[List[int]]:
    result = []  # List to store the result (subsets that sum to k)

    # Helper function that uses backtracking to explore subsets
    def backtrack(start, path, total):
        # If the total sum of the current path equals 'k', add it to the result
        if total == k:
            result.append(path[:])  # Append a copy of the current path to result
            return
        # If the total exceeds 'k', there's no need to explore further
        if total > k:
            return

        # Loop through the array starting from the current 'start' index
        for i in range(start, len(arr)):
            # Add current number to path and update total
            path.append(arr[i])
            # Recursively call backtrack with the new total and the updated path
            backtrack(i + 1, path, total + arr[i])
            # Remove the last element from path (backtracking)
            path.pop()

    # Start the backtracking process from index 0 with an empty path and total 0
    backtrack(0, [], 0)
    # Return the list of subsets that sum to 'k'
    return result


def get_k_sum_subsets_with_bit(
    set_of_integers: List[int], target_sum: int
) -> List[List[int]]:
    # function that checks whether the specified bit is on in the specified number
    def get_bit(num, bit):
        temp = 1 << bit
        temp = temp & num
        if temp == 0:
            return 0
        return 1

    subsets = []
    subsets_count = 2 ** len(set_of_integers)
    for i in range(0, subsets_count):
        sum_ = 0
        subset = []

        for j in range(0, len(set_of_integers)):
            # if the jth number should be included in this subset
            if get_bit(i, j) == 1:
                # add it to the sum
                sum_ = sum_ + set_of_integers[j]
                # and check it against the target
                if sum_ > target_sum:
                    # reject the jth number if the sum exceeds the target
                    break
                subset.append(set_of_integers[j])
        if sum_ == target_sum:
            # if the sum matches the target, save the candidate subset as a valid solution
            subsets.append(subset)

    return subsets
