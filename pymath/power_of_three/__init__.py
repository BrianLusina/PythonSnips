from math import log


def is_power_of_three_with_log(n: int) -> bool:
    if n < 1:
        return False

    k = log(n, 3)
    k_round = int(round(k))
    return 3**k_round == n


def is_power_of_three_with_mod(n: int) -> bool:
    # The largest power of 3 within 32-bit signed integer range is 3^19 = 1162261467
    # If n is a power of 3, then 1162261467 % n must equal 0
    # We also need n to be positive since negative numbers and zero can't be powers of 3
    return n > 0 and 1162261467 % n == 0


def is_power_of_three_with_loop(n: int) -> bool:
    # Keep dividing by 3 while n is greater than 2
    while n > 2:
        # If n is not divisible by 3, it's not a power of 3
        if n % 3 != 0:
            return False
        # Divide n by 3 using integer division
        n //= 3

    # After the loop, n should be 1 if it was a power of 3
    # (since 3^0 = 1)
    return n == 1
