def gibonacci(n: int, x: int, y: int) -> int:
    if n == 0:
        return x

    g0 = x
    g1 = y
    current = g1 - g0

    for _ in range(n - 1):
        current = g1 - g0
        g0 = g1
        g1 = current

    return current
