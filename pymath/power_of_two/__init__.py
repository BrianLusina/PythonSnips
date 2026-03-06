def is_power_of_two(n: int) -> bool:
    # Perform bitwise AND between n and (n - 1)
    # This will be 0 only if n has exactly one 1-bit in its binary form
    return n > 0 and (n & (n - 1)) == 0
