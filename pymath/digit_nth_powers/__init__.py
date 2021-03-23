def digit_nth_power(nth):
    """
    Finds the sum of all numbers that can be written as the sum of nth power of their digits.
    Uses Brute force to find the sum of all numbers. We first need to find the limit/upper bound. To do that we
    The highest digit is 9  and 9^5=59049 , which has five digits. If we then look at 5 \times 9^5=295245 ,
    which has six digits and a good endpoint for the loop (in the case of nth = 5)

    >>> digit_nth_power(4)
    19316

    :param nth: Power of each digit
    :type nth int
    :return: sum of all numbers
    :raises: ValueError
    :rtype: int
    """
    if nth is None or not isinstance(nth, int):
        raise ValueError("Expected nth power to be an integer")

    # this finds the limit we will use for brute force
    limit = 6 * 9 ** nth

    result = []

    for number in range(10, limit):
        total = 0
        number_str = str(number)

        total += sum(int(num) ** nth for num in number_str)

        if total == number:
            result.append(number)

    return sum(result)


if __name__ == "__main__":
    power = 5
    sum_of_numbers = digit_nth_power(power)
    print(f"Sum of all numbers that can be written as the sum of {power} of their digits is {sum_of_numbers}")
