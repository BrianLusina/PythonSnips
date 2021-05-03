from typing import List


def self_dividing_numbers(left: int, right: int) -> List[int]:
    """
    Alternate implementation of self_dividing:
    def self_dividing(n):
        x = n
        while x > 0:
            x, d = divmod(x, 10)
            if d == 0 or n % d > 0:
                return False
        return True
    """

    def self_dividing(number: int):
        for digit in str(number):
            if digit == '0' or number % int(digit) > 0:
                return False
        return True

    result = []

    for num in range(left, right + 1):
        if self_dividing(num):
            result.append(num)

    return result  # or filter(self_dividing, range(left, right + 1)
