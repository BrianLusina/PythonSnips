from functools import reduce


def largest_product(num_str, sub_length):
    """
    Passes the number string and substring length to the slice_me() function
    looping though each substring to obtain the maximum possible product
    :param num_str:
    :param sub_length:
    :return: largest product
    """
    return max(reduce(lambda x, y: x * y, sli) for sli in slice_me(num_str, sub_length)) \
        if sub_length != 0 else 1


def slice_me(series, length):
    """
    Performs the validation for the length to slice through,
    if the length is out of the bound (1, len(series)) raise a ValueError
    else get consecutive substrings from the series
    :param series:
    :param length:
    :return: slices of the series
    """
    numbers = [int(digit) for digit in series]
    if not 1 <= length <= len(series):
        raise ValueError("Invalid length to slice %s" % str(length))
    return [numbers[i: i + length] for i in range(len(numbers) - length + 1)]
