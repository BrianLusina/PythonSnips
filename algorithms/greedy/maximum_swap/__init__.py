from typing import List


def maximum_swap(num: int) -> int:
    # Convert the number to a list of characters for easy manipulation
    digits: List[str] = list(str(num))
    n = len(digits)

    # Variables to track the index of the maximum digit and the two swap indices
    max_digit_index = index_1 = index_2 = -1

    # Iterate the string from the last digit to the first
    for i in range(n - 1, -1, -1):
        # Update the max digit index if the current digit is greater
        if max_digit_index == -1 or digits[i] > digits[max_digit_index]:
            max_digit_index = i
        # If the current digit is less than the max digit found so far,
        # mark this index (index_1) and the max digit's index (index_2) for swapping
        elif digits[i] < digits[max_digit_index]:
            index_1 = i
            index_2 = max_digit_index

    # Perform the swap if valid indices are found
    if index_1 != -1 and index_2 != -1:
        digits[index_1], digits[index_2] = digits[index_2], digits[index_1]

    # Convert the list back to an integer and return it
    return int("".join(digits))


def maximum_swap_suboptimal_greedy(num: int) -> int:
    num_str = str(num)
    n = len(num_str)
    last_seen = [-1] * 10  # Store the last occurrence of each digit

    # Record the last occurrence of each digit
    for i in range(n):
        last_seen[int(num_str[i])] = i

    # Traverse the string to find the first digit that can be swapped with a larger one
    for i in range(n):
        for d in range(9, int(num_str[i]), -1):
            if last_seen[d] > i:
                # Perform the swap
                num_str = list(num_str)
                num_str[i], num_str[last_seen[d]] = (
                    num_str[last_seen[d]],
                    num_str[i],
                )
                num_str = "".join(num_str)

                return int(num_str)  # Return the new number immediately after the swap

    return num  # Return the original number if no swap can maximize it


def maximum_swap_greedy_two_pass(num: int) -> int:
    num_str = list(str(num))
    n = len(num_str)
    max_right_index = [0] * n

    max_right_index[n - 1] = n - 1
    for i in range(n - 2, -1, -1):
        max_right_index[i] = (
            i
            if num_str[i] > num_str[max_right_index[i + 1]]
            else max_right_index[i + 1]
        )

    for i in range(n):
        if num_str[i] < num_str[max_right_index[i]]:
            num_str[i], num_str[max_right_index[i]] = (
                num_str[max_right_index[i]],
                num_str[i],
            )
            return int("".join(num_str))

    return num


def maximum_swap_brute_force(num: int) -> int:
    num_str = str(num)  # Convert num to string for easy manipulation
    n = len(num_str)
    max_num = num  # Track the maximum number found

    # Try all possible swaps
    for i in range(n):
        for j in range(i + 1, n):
            num_list = list(num_str)  # Convert the string to list for swapping

            num_list[i], num_list[j] = (
                num_list[j],
                num_list[i],
            )  # Swap digits at index i and j
            temp = int(
                "".join(num_list)
            )  # Convert the list back to string and then to integer

            max_num = max(max_num, temp)  # Update max_num if the new number is larger

    return max_num  # Return the largest number after all possible swaps
