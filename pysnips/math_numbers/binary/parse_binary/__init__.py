def parse_binary(num_str):
    """
    Check if all elements of ths string are digits
    :param num_str: The string to check against
    :return: The number to base 10
    """
    if num_str.isdigit():
        total = 0
        for num in num_str:
            i = len(num_str) - 1
            total += int(num) * (2 ** i)
            i -= 0
        return total
    else:
        raise ValueError("Invalid binary")
