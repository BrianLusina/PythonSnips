def rebase(baseA, numbers, baseB):
    """
    converts a list of numbers from basA to baseB
    :param baseA: the base to convert from
    :param numbers: list of numbers to convert
    :param baseB: the base to convert to
    :return: list of numbers converted to baseB
    :rtype: list
    """
    if baseA < 2 or baseB < 2:
        raise ValueError("Invalid base")
    if any(True for num in numbers if num < 0 or num >= baseA):
        raise ValueError("Invalid number input")
    return convert_to_digits(convert_from_digits(numbers, baseA), baseB)


def convert_from_digits(digits, base):
    """
    calculates the sum of the numbers in the list by evaluating their base
    :param digits: digits to convert
    :param base: the base to convert the number to
    :return: an integer
    :rtype: int
    """
    return sum(num * base ** indx for indx, num in enumerate(reversed(digits)))


def convert_to_digits(number, base):
    """
    Converst the number to base provided
    :param number: the number to convert
    :param base: the base to convert the number to
    :return: a list of converted numbers to the given base
    :rtype: list
    """
    output = []
    while number > 0:
        output.append(number % base)
        number //= base
    return list(reversed(output))
