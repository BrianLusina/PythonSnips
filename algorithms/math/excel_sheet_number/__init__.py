def title_to_number(column_title: str) -> int:
    """
    Convert Excel column title to number

    Args:
        column_title(str): Excel column title (e.g. A, B, AA, AB, ...)
    Returns:
        Corresponding column number (1-indexed)
    """
    result = 0

    # iterate through each character in the column title
    for char in column_title:
        # Convert character to its position in the alphabet
        char_value = ord(char) - ord("A") + 1

        # Build the result using base-26 conversion. Similar to converting "123" to decimal: 1*10^2 + 2*10^1 + 3*10^0
        # Here we do: previous_result * 26 + current_char_value
        result = result * 26 + char_value

    return result
