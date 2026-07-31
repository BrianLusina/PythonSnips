def my_pow(x: float | int, n: int) -> float:
    def power(base: float | int, exponent: int) -> float:
        result = 1.0

        # process each bit of the exponent
        while exponent > 0:
            # if current bit is 1, multiply result by current base
            if exponent & 1:  # check if lest significant bit is 1
                result *= base

            # Square the base for the next bit position
            base *= base

            # Right shift to process the next bit
            exponent >>= 1
        return result

    # Handle negative exponents by computing 1 / (x^(-n))
    if n >= 0:
        return power(x, n)
    else:
        return 1.0 / power(x, -n)


def my_pow_rec(x: float | int, n: int) -> float:
    # Helper function using fast exponentiation (binary exponentiation)
    def fast_pow(base: float | int, exp: int):
        # Base case: any number to the power of 0 is 1
        if exp == 0:
            return 1.0
        # Recursively compute half power
        half = fast_pow(base, exp // 2)
        # If exponent is even, square the half result
        if exp % 2 == 0:
            return half * half
        # If exponent is odd, multiply by base once more
        else:
            return half * half * base

    # Handle negative exponents by inverting x and using positive n
    if n < 0:
        x = 1.0 / x
        n = -n

    # Return the computed power
    return fast_pow(x, n)


def my_pow_iter(x: float | int, n: int) -> float | int:
    # Handle negative exponent
    if n < 0:
        x = 1 / x
        n = -n

    res = 1.0
    current_product = x
    while n > 0:
        # If n is odd, multiply the result by the current product
        if n % 2 == 1:
            res *= current_product
        # Square the product and halve the exponent
        current_product *= current_product
        n //= 2
    return res
