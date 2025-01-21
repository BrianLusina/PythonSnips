def str_to_int(input_str: str) -> int:
    """
    Converts an input string int an integer
    Args:
        input_str(str): input string
    Returns:
        int integer representation of the input string
    """
    output_int = 0

    if input_str[0] == '-':
        is_negative = True
    else:
        is_negative = False

    str_len = len(input_str)
    l = str_len - 1 if is_negative else str_len
    str_to_convert = input_str[1:] if is_negative else input_str

    for index, char in enumerate(str_to_convert):
        unicode = ord(char) - ord('0')
        exponent = l - (index + 1)
        number = unicode * 10**exponent
        output_int += number

    return output_int *-1 if is_negative else output_int
