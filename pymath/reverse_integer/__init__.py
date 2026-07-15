def reverse_int(num: int) -> int:
    sign = [1, -1][num < 0]
    rev, abs_num = 0, abs(num)
    while abs_num:
        abs_num, mod = divmod(abs_num, 10)
        rev = rev * 10 + mod
        if rev > 2**31 - 1:
            return 0
    return sign * rev


def reverse_int_2(num: int) -> int:
    # Define the maximum value for a 32-bit signed integer
    INT_MAX = 2**31 - 1

    # Initialize result to 0, which will store the reversed number
    result = 0

    # Check if the number is negative
    is_negative = num < 0

    # Work with the absolute value of num for simplicity
    if is_negative:
        num = -num

    # Loop through the digits of the number until num becomes 0
    while num != 0:
        # Extract the last digit of num
        digit = num % 10

        # Remove the last digit from num
        num //= 10

        # Check for overflow before updating the result
        # If adding the digit will cause an overflow, return 0
        if result > (INT_MAX - digit) // 10:
            return 0

        # Update the result by shifting the previous digits and adding the new digit
        result = result * 10 + digit

    # Return the result with the correct sign
    return -result if is_negative else result
