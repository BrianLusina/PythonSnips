from math import gcd


def coprime(a, b):
    return True if gcd(a, b) == 1 else False


def cycle(n):
    if n % 2 == 0 or not coprime(n, 10):
        return -1

    rem = 1

    for _ in range(1, n + 2):
        rem = (10 * rem) % n

    d = rem
    count = 0
    rem = (10 * rem) % n
    count += 1

    while rem != d:
        rem = (10 * rem) % n
        count += 1

    return count
