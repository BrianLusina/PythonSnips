from typing import List


def int_to_str(input_int: int) -> str:
    """
    Converts an integer to a string
    Args:
        input_int (int): input integer
    Returns:
        str: input integer as a string
    """

    # check if the input integer is negative
    if input_int < 0:
        # if it is, convert it to a positive integer by multiplying it by -1
        is_negative = True
        input_int *= -1
    else:
        is_negative = False

    output_str: List[str] = []

    # if the input integer is 0, then simply append '0' to the output result
    if input_int == 0:
        output_str.append("0")
    else:
        # if not, then the last digit of the input integer is extracted using the % operator. e.g. 12 % 10 = 2, 17%10=7
        # Taking the modulus of a number with 10, always gets the last digit of that number.
        # The last digit is converted into a character by the chr() and the ord() functions. so ord('0') + last_digit
        # gives the unicode code point of the character that we want which when passed to chr() function returns a
        # character. The character is then appended to the output_str.
        # As we have now dealt with the last digit already, we remove it using th // operator.
        # This repeats until the input integer is less than or equal to 0
        while input_int > 0:
            last_digit = input_int % 10
            unicode = ord("0") + last_digit
            character = chr(unicode)
            output_str.append(character)
            input_int //= 10

        # reverses the positions of its elements so that the last digit is on the last index of the output_str
        output_str = output_str[::-1]

    # join the elements together
    result = "".join(output_str)

    # deal with the sign. Add - if it was a negative integer or simply return the result if it was a positive integer.
    if is_negative:
        return "-" + result
    else:
        return result
