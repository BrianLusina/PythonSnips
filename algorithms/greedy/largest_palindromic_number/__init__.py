from collections import Counter


def largest_palindromic_number(num: str) -> str:
    # Count the frequency of each digit in the input string
    occureneces = Counter(num)

    # first half and the middle of the palindrome
    first_half = []
    middle = ""

    for digit in range(9, -1, -1):
        digit_char = str(digit)

        if digit_char in occureneces:
            digit_count = occureneces[digit_char]

            # num of pairs of this digit that can be used
            num_pairs = digit_count // 2

            # If pairs available, add them to the first half
            if num_pairs:
                # Avoiding leading zeros
                if not first_half and not digit:
                    occureneces["0"] = 1
                else:
                    first_half.append(digit_char * num_pairs)

            # Checking for a middle element
            if digit_count % 2 and not middle:
                middle = digit_char

    # If all elements are '0'
    if not middle and not first_half:
        return "0"

    # Returning the full palindrome
    return "".join(first_half + [middle] + first_half[::-1])


def largest_palindromic_number_v2(num: str) -> str:
    # Count how many times each digit appears
    digit_counter = Counter(num)

    result = ""
    # Find the middle digit by counting down from 9 to 0 while decrementing the count of a digit that appears an odd
    # number of times
    for digit in range(9, 0, -1):
        digit_str = str(digit)
        if digit_counter[digit_str] % 2 == 1:
            result = digit_str
            # decrement the count of this digit
            digit_counter[digit_str] -= 1
            break

    # Build symmetric pairs by iterating from 0 to 9 for each digit with remaining count
    for number in range(10):
        number_str = str(number)
        if digit_counter[number_str] > 0:
            # Divide by two to get number of pairs
            digit_counter[number_str] //= 2
            temp = digit_counter[number_str] * number_str
            result = f"{temp}{result}{temp}"

    return result.strip("0") or "0"
