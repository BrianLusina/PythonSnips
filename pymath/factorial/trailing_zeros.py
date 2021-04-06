def zeros(n: int) -> int:
    count = 0
    while n >= 5:
        n //= 5
        count += n
    return count
