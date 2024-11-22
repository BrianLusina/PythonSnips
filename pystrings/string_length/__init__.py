def iterative_string_len(input_str: str) -> int:
    """
    Calculates a string's length using an iterative approach

    Args:
        input_str (str): input string
    Returns:
        int: length of an input string
    """
    count = 0
    for _ in input_str:
        count += 1
    return count

def recursive_string_len(input_str: str) -> int:
    """
    Calculates a string's length using a recursive approach

    Args:
        input_str (str): input string
    Returns:
        int: length of an input string
    """
    if input_str == "":
        return 0
    return 1 + recursive_string_len(input_str[1:])