def integer_addition(a: int, b: int):
    # Mask to limit the result to 32-bits (the size of an integer in Python)
    mask = 0xFFFFFFFF
    # Setting maximum integer value
    max_int = 0x7FFFFFFF

    while b != 0:
        # Sum of the integers without carrying
        result = (a ^ b) & mask

        # Calculate the carry that needs to be added to the next pair of integers
        carry = ((a & b) << 1) & mask

        # Update a and b to the new values for the next iteration
        a = result
        b = carry

    # We check if the result is greater than the maximum integer value
    # Return the result as is if result is not greater than max_int
    if a < max_int:
        return a

    # If it is, then return the two's complement of the result
    else:
        return ~(a ^ mask)


def integer_addition_2(a: int, b: int) -> int:
    mask = 0xFFFFFFFF
    max_int = 2 ** 31 - 1
    while b != 0:
        sum_ = (a ^ b) & mask
        carry = (a & b) & mask
        a = sum_
        b = carry << 1
    return a if a <= max_int else ~(a ^ mask)