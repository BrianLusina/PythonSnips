def count_bits(n: int) -> int:
    count = 0

    while n:
        # Check the least significant bit by using AND
        if n & 1:
            count += 1
        # Right-shift the number to move to the next bit
        n >>= 1

    return count
