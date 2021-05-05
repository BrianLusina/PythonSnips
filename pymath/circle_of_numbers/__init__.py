def circle_of_numbers(n: int, first_number: int) -> int:
    """
    First off, to get to other side, first off you'd want to divide n by 2, then offset it by firstNumber. To account
    for the rotation, you basically want to find the remainder after dividing it because it's always goin to a value
    between 0 and n, which is where modulus comes in.
    """
    return (first_number + (n // 2)) % n
