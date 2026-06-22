from typing import List


def add_negabinary(arr1: List[int], arr2: List[int]) -> List[int]:
    # Initialize pointers to the least significant bits(rightmost elements)
    index_1, index_2 = len(arr1) - 1, len(arr2) - 1

    # Initialize carry value for addition
    carry = 0

    # Result to store the sum digits
    result = []

    # Process digits from right to left, including any remaining carry
    while index_1 >= 0 or index_2 >= 0 or carry != 0:
        # Get current digit from arr1, or 0 if we've exhausted arr1
        digit_1 = 0 if index_1 < 0 else arr1[index_1]

        # Get current digit from arr2, or 0 if we've exhausted arr2
        digit_2 = 0 if index_2 < 0 else arr2[index_2]

        # Calculate sum of current position including carry
        current_sum = digit_1 + digit_2 + carry

        # Reset carry for next iteration
        carry = 0

        # Handle negabinary addition rules
        if current_sum >= 2:
            # If sum is 2 or more, subtract 2 and set negative carry
            current_sum -= 2
            carry = -1
        elif current_sum == -1:
            # If sum is -1, set digit to 1 and positive carry
            current_sum = 1
            carry = 1

        # Append the computed digit to result
        result.append(current_sum)

        # Move pointest to the next more significant bits
        index_1 -= 1
        index_2 -= 1

    # Remove leading zeros from the result (except if result is just [0]
    while len(result) > 1 and result[-1] == 0:
        result.pop()

    # Reverse the result since we built it from least to most significant
    return result[::-1]


def add_negabinary_2(arr1: List[int], arr2: List[int]) -> List[int]:
    arr1 = arr1[::-1]
    arr2 = arr2[::-1]

    max_len = max(len(arr1), len(arr2))

    result = []
    carry = 0

    i = 0
    while i < max_len or carry != 0:
        bit1 = arr1[i] if i < len(arr1) else 0
        bit2 = arr2[i] if i < len(arr2) else 0

        total = bit1 + bit2 + carry

        if total >= 0:
            result.append(total % 2)
            carry = -(total // 2)
        else:
            result.append(1)
            carry = 1

        i += 1

    while len(result) > 1 and result[-1] == 0:
        result.pop()

    return result[::-1]
